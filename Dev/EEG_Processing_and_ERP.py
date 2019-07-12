# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:39:26 2019

@author: Julian, Yiwen
"""
from converter import converter
from filters import filters
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import mne

# Events: 1 = yes/blink, 2 = eyes/close
events = np.array([[2500, 0, 1],
                   [3750, 0, 1],
                   [5000, 0, 2]])

freqs = [
    ('Theta', 4, 7),
    ('Alpha', 8, 13),
    ('Beta', 13, 25),
    ('Gamma', 30, 45)
]

# Load raw fif data
<<<<<<< HEAD
raw = mne.io.read_raw_fif("../Data/06_25/fif/OpenBCI-RAW-06_25_1.fif", preload=True)
=======
raw = mne.io.read_raw_fif("../Data/06_25/fif/OpenBCI-RAW-06_25_6.fif", preload=True)
>>>>>>> ccf02f827875ee4d3adb76d82ae7ee3a2d2b75f0

# Apply high-pass (1 Hz), alpha band filter, and notch filter (60 hz)
##raw.notch_filter(60)
##band, fmin, fmax = freqs[1]
##raw.filter(fmin, fmax, n_jobs=1,  # use more jobs to speed up.
##           l_trans_bandwidth=1,  # make sure filter params are the same
##           h_trans_bandwidth=1,  # in each band and skip "auto" option.
##           fir_design='firwin')

# Apply high-pass (1 Hz), alpha band filter, and notch filter (60 hz)
##band, fmin, fmax = freqs[1]
##raw_data = raw.get_data()
##length = np.arange(1, raw_data.shape[-1]+1)
##plt.plot(length, raw_data[0])
##plt.show()
##raw_data = filters.notch_filter(raw_data)
##plt.plot(length, raw_data[0])
##plt.show()
##raw_data = filters.bandpass_filter(raw_data, fmin, fmax)
##plt.plot(length, raw_data[0])
##plt.show()
##raw_fft = filters.fft(raw_data)
##plt.plot(length, raw_fft[0])
##plt.show()

# Apply high-pass (1 Hz), alpha band filter, and notch filter (60 hz)
band, fmin, fmax = freqs[1]
raw_data = raw.get_data()
<<<<<<< HEAD
raw_data = raw_data[:, raw.time_as_index(22)[0]:] # after 22s
##length = np.arange(1, raw_data.shape[-1]+1)
length = raw.times[raw.time_as_index(22)[0]:]

##plt.subplot(5, 1, 1)
##plt.plot(length, raw_data[0])
##plt.title("raw data")
##plt.grid(True)
##
##plt.subplot(5, 1, 2)
##raw_data = filters.notch_filter(raw_data)
##plt.plot(length, raw_data[0])
##plt.title("notch filter")
##plt.grid(True)
##
##plt.subplot(5, 1, 5)
##raw_fft = np.fft.fft(raw_data)
##plt.plot(length, raw_fft[0])
##plt.title("fft notch filter")
##plt.grid(True)
##
##plt.subplot(5, 1, 3)
##raw_data = filters.bandpass_filter(raw_data, fmin, fmax)
##plt.plot(length, raw_data[0])
##plt.title("bandpass filter")
##plt.grid(True)
##
##plt.subplot(5, 1, 4)
##raw_fft = filters.fft(raw_data)
##plt.plot(length, raw_fft[0])
##plt.title("fft")
##plt.grid(True)
##
##plt.tight_layout()
##plt.show()

##plt.subplot(4, 1, 1)
##plt.plot(length, raw_data[0])
##plt.title("raw data")
##plt.grid(True)
##
##plt.subplot(4, 1, 2)
##raw_data = filters.notch_filter(raw_data)
##plt.plot(length, raw_data[0])
##plt.title("notch filter")
##plt.grid(True)
##
##plt.subplot(4, 1, 3)
##raw_data = filters.bandpass_filter(raw_data, fmin, fmax)
##plt.plot(length, raw_data[0])
##plt.title("bandpass filter")
##plt.grid(True)
##
##plt.subplot(4, 1, 4)
##raw_fft = filters.fft(raw_data)
##plt.plot(length, raw_fft[0])
##plt.title("fft")
##plt.grid(True)
##
##plt.tight_layout()
##plt.show()


plt.plot(length, raw_data[0])
plt.ylabel("mV")
plt.xlabel("Time [s]")
plt.show()

raw_data = filters.notch_filter(raw_data)
plt.plot(length, raw_data[0])
plt.ylabel("mV")
plt.xlabel("Time [s]")
plt.show()

raw_data = filters.bandpass_filter(raw_data, fmin, fmax)
plt.plot(length, raw_data[0])
plt.ylabel("mV")
plt.xlabel("Time [s]")
plt.show()

frq, raw_fft = filters.fft(raw_data)
fig = plt.plot(frq, raw_fft[0])
##plt.xscale("log")
##plt.yscale("log")
plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.show()
=======
raw_data = raw_data[:, 5200:]
length = np.arange(1, raw_data.shape[-1]+1)

##plt.subplot(5, 1, 1)
##plt.plot(length, raw_data[0])
##plt.title("raw data")
##plt.grid(True)
##
##plt.subplot(5, 1, 2)
##raw_data = filters.notch_filter(raw_data)
##plt.plot(length, raw_data[0])
##plt.title("notch filter")
##plt.grid(True)
##
##plt.subplot(5, 1, 5)
##raw_fft = np.fft.fft(raw_data)
##plt.plot(length, raw_fft[0])
##plt.title("fft notch filter")
##plt.grid(True)
##
##plt.subplot(5, 1, 3)
##raw_data = filters.bandpass_filter(raw_data, fmin, fmax)
##plt.plot(length, raw_data[0])
##plt.title("bandpass filter")
##plt.grid(True)
##
##plt.subplot(5, 1, 4)
##raw_fft = filters.fft(raw_data)
##plt.plot(length, raw_fft[0])
##plt.title("fft")
##plt.grid(True)
##
##plt.tight_layout()
##plt.show()

##plt.subplot(4, 1, 1)
##plt.plot(length, raw_data[0])
##plt.title("raw data")
##plt.grid(True)
##
##plt.subplot(4, 1, 2)
##raw_data = filters.notch_filter(raw_data)
##plt.plot(length, raw_data[0])
##plt.title("notch filter")
##plt.grid(True)
##
##plt.subplot(4, 1, 3)
##raw_data = filters.bandpass_filter(raw_data, fmin, fmax)
##plt.plot(length, raw_data[0])
##plt.title("bandpass filter")
##plt.grid(True)
##
##plt.subplot(4, 1, 4)
##raw_fft = filters.fft(raw_data)
##plt.plot(length, raw_fft[0])
##plt.title("fft")
##plt.grid(True)
##
##plt.tight_layout()
##plt.show()


plt.plot(length, raw_data[0])
plt.show()
raw_data = filters.notch_filter(raw_data)
plt.plot(length, raw_data[0])
plt.show()
raw_data = filters.bandpass_filter(raw_data, fmin, fmax)
plt.plot(length, raw_data[0])
plt.show()

frq, raw_fft = filters.fft(raw_data)
fig = plt.plot(frq, raw_fft[1])
plt.xscale("log")
plt.yscale("log")
plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.show()



# Remove reference from raw obj; prevent MNE from adding EEG average reference.
raw_no_ref, _ = mne.set_eeg_reference(raw, [])

# Define epochs and set ERP for 'eyes/bylink' event
reject = dict(eeg=180e-6)
event_id, tmin, tmax = {'eyes/close': 2}, -10., 10.
epochs_params = dict(events=events, event_id=event_id, tmin=tmin, tmax=tmax,
                     reject=None)
>>>>>>> ccf02f827875ee4d3adb76d82ae7ee3a2d2b75f0

##plt.bar(frq.shape[-1], raw_fft[0])
##plt.show()

### Remove reference from raw obj; prevent MNE from adding EEG average reference.
##raw_no_ref, _ = mne.set_eeg_reference(raw, [])
##
### Define epochs and set ERP for 'eyes/bylink' event
##reject = dict(eeg=180e-6)
##event_id, tmin, tmax = {'eyes/close': 2}, -10., 10.
##epochs_params = dict(events=events, event_id=event_id, tmin=tmin, tmax=tmax,
##                     reject=None)
##
##evoked_no_ref = mne.Epochs(raw_no_ref, **epochs_params).average()
##del raw_no_ref  # save memory
##
##title = 'EEG Original reference'
##evoked_no_ref.plot(titles=dict(eeg=title), time_unit='s')
### Need montage to create topomap:
### evoked_no_ref.plot_topomap(times=[0.1], size=3., title=title, time_unit='s')

