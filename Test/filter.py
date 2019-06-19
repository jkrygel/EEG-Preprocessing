import mne
import pandas
import numpy as np
from mne.io import read_raw_bdf
from mne.filter import notch_filter

# raw data
dat = read_raw_bdf("../Data/Subject_1-1.bdf")
event = mne.events_from_annotations(dat)

# print(dat.info)
# dat.plot()

# use EEG channel 1 to test
# eeg1 = dat.to_data_frame("EEG 1")

# apply notch filter, not sure about the parameters
# notch_filter(eeg1.values, 250, np.arange(60, 121, 60))
