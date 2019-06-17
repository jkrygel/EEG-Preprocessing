import pandas
import numpy as np
from mne.io import read_raw_bdf
from mne.filter import notch_filter

# raw data
dat = read_raw_bdf("Subject_1-1.bdf")
print(dat.info)
##dat.plot()

# use EEG channel 1 to test
eeg1 = dat.to_data_frame("EEG 1")

# apply notch filter, not sure about the parameters
notch_filter(eeg1.values, 60, np.arange(12, 30))

##Error: ValueError: The requested filter length 397 is too short for the requested 0.18 Hz transition band, which requires 555 samples
