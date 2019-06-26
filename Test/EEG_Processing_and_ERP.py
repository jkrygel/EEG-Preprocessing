# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:39:26 2019

@author: Julian, Yiwen
"""

import numpy as np
import mne

# Events: 1 = yes/blink, 2 = eyes/close
events = np.array([[2500, 0, 1],
                   [3750, 0, 1],
                   [5000, 0, 2]])

# Load txt data, add info and create raw
raw_data = '..\Data\OpenBCI-RAW-06_25_1.txt'
data = np.loadtxt(raw_data, delimiter=',', skiprows=6, 
                  usecols=tuple(range(1,9)))

ch_names = ['EEG1','EEG2','EEG3','EEG4','EEG5','EEG6','EEG7','EEG8']  
sfreq = 250  # Hz
info = mne.create_info(ch_names, sfreq)
raw = mne.io.RawArray(data.T, info)

for i in range(1,9):
    name = 'EEG' + str(i)
    raw.set_channel_types(mapping={f'{name}': 'eeg'})

freqs = [
    ('Theta', 4, 7),
    ('Alpha', 8, 13),
    ('Beta', 13, 25),
    ('Gamma', 30, 45)
]

# Apply high-pass (1 Hz), alpha band filter, and notch filter (60 hz)
raw.notch_filter(60)
band, fmin, fmax = freqs[1]
raw.filter(fmin, fmax, n_jobs=1,  # use more jobs to speed up.
           l_trans_bandwidth=1,  # make sure filter params are the same
           h_trans_bandwidth=1,  # in each band and skip "auto" option.
           fir_design='firwin')

# Remove reference from raw obj; prevent MNE from adding EEG average reference.
raw_no_ref, _ = mne.set_eeg_reference(raw, [])

# Define epochs and set ERP for 'eyes/bylink' event
reject = dict(eeg=180e-6)
event_id, tmin, tmax = {'eyes/close': 2}, -2., 2.
epochs_params = dict(events=events, event_id=event_id, tmin=tmin, tmax=tmax,
                     reject=None)

evoked_no_ref = mne.Epochs(raw_no_ref, **epochs_params).average()
del raw_no_ref  # save memory

title = 'EEG Original reference'
evoked_no_ref.plot(titles=dict(eeg=title), time_unit='s')
# Need montage to create topomap:
# evoked_no_ref.plot_topomap(times=[0.1], size=3., title=title, time_unit='s')

