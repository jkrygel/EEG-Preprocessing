# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:39:26 2019

@author: Julian Krygel
"""

import numpy as np
import mne
from mne.filter import notch_filter

# Create event at eyes closing @ about 30s into recording
events = np.array([[7750, 0, 1]])

# Load data
raw_data = '..\Data\Subject_1-1.bdf'
raw = mne.io.read_raw_bdf(raw_data, preload=True)

# Only look at eeg channels
raw.pick_types(meg=False, eeg=True)

# Drop accelerometer channels (MNE reads them as eeg chanels? idk)
raw.drop_channels(('Accel X', 'Accel Y', 'Accel Z'))
# Apply notch at 60 Hz for power grid interference
raw.notch_filter(60)

# Remove reference from raw object to prevent MNE from adding a default EEG 
# average reference.
raw_no_ref, _ = mne.set_eeg_reference(raw, [])

# Define epochs and set ERP for 'Eyes/close' event
# reject = dict(eeg=180e-6)
event_id, tmin, tmax = {'Eyes/close': 1}, -0.5, 0.5
epochs_params = dict(events=events, event_id=event_id, tmin=tmin, tmax=tmax,
                     reject=None)

evoked_no_ref = mne.Epochs(raw_no_ref, **epochs_params).average()
del raw_no_ref  # save memory

title = 'EEG Original reference'
evoked_no_ref.plot(titles=dict(eeg=title), time_unit='s')
# Need montage to create topomap
# evoked_no_ref.plot_topomap(times=[0.1], size=3., title=title, time_unit='s')