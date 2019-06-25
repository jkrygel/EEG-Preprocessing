# -*- coding: utf-8 -*-

import numpy as np
import mne
from mne.filter import notch_filter

# Location
raw_data = '..\Data\Subject_1-1.bdf'

# Frequency Bands
iter_freqs = [
    ('Theta', 4, 7),
    ('Alpha', 8, 12),
    ('Beta', 13, 25),
    ('Gamma', 30, 45)
]

# Epoching parameters
event_id, tmin, tmax = 1, -1., 1.
baseline = None

# Make events
events = np.array([[7750, 0, 1]])

frequency_map = list()

for band, fmin, fmax in iter_freqs:
    # Reload the data to save memory, use preload=True
    raw = mne.io.read_raw_bdf(raw_data, preload=True)
    raw.pick_types(meg=False, eeg=True)  # only look at eeg channels
    # Drop accelerometer channels (MNE reads them as eeg chanels? idk)
    raw.drop_channels(('Accel X', 'Accel Y', 'Accel Z'))
    
    # bandpass + notch filter and compute Hilbert
    raw.filter(fmin, fmax,
               l_trans_bandwidth='auto', # make sure filter params are the same
               h_trans_bandwidth='auto', # in each band and skip "auto" option.
               fir_design='firwin')
    raw.notch_filter(60)
    raw.apply_hilbert(envelope=False)
        
    epochs = mne.Epochs(raw, events, event_id, tmin, tmax, baseline=baseline,
                        preload=True)    
    
    # remove evoked response and get analytic signal (envelope)
    epochs.subtract_evoked()  # for this we need to construct new epochs.
    epochs = mne.EpochsArray(
        data=np.abs(epochs.get_data()), info=epochs.info, tmin=epochs.tmin)
    # now average and move on
    frequency_map.append(((band, fmin, fmax), epochs.average()))
    
fig, axes = plt.subplots(4, 1, figsize=(10, 7), sharex=True, sharey=True)
colors = plt.get_cmap('winter_r')(np.linspace(0, 1, 4))
for ((freq_name, fmin, fmax), average), color, ax in zip(
        frequency_map, colors, axes.ravel()[::-1]):
    times = average.times * 1e3
    gfp = np.sum(average.data ** 2, axis=0)
    gfp = mne.baseline.rescale(gfp, times, baseline=(None, 0))
    ax.plot(times, gfp, label=freq_name, color=color, linewidth=2.5)
    ax.axhline(0, linestyle='--', color='grey', linewidth=2)
    ci_low, ci_up = _bootstrap_ci(average.data, random_state=0,
                                  stat_fun=lambda x: np.sum(x ** 2, axis=0))
    ci_low = rescale(ci_low, average.times, baseline=(None, 0))
    ci_up = rescale(ci_up, average.times, baseline=(None, 0))
    ax.fill_between(times, gfp + ci_up, gfp - ci_low, color=color, alpha=0.3)
    ax.grid(True)
    ax.set_ylabel('GFP')
    ax.annotate('%s (%d-%dHz)' % (freq_name, fmin, fmax),
                xy=(0.95, 0.8),
                horizontalalignment='right',
                xycoords='axes fraction')
    ax.set_xlim(-1000, 1000)
    ax.set_ylim(0.0001, -0.0001)

axes.ravel()[-1].set_xlabel('Time [ms]')
