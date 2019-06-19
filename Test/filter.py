import mne
import pandas
import numpy as np
from mne.io import read_raw_bdf
from mne.filter import notch_filter

# raw data
dat = read_raw_bdf("../Data/Subject_1-1.bdf", preload=True)
event = mne.events_from_annotations(dat)
info = dat.info
sfreq = info.get("sfreq")

# apply notch filter only on 60 Hz, default setting of OpenBCI
# https://martinos.org/mne/stable/generated/mne.io.Raw.html?highlight=notch#mne.io.Raw.notch_filter
dat.notch_filter(60)

# bandpass filter (Beta)
dat.filter(13, 25, n_jobs=1,        # use more jobs to speed up
            l_trans_bandwidth=1,    # make sure filter params are the same
            h_trans_bandwidth=1,    # in each band and skip "auto" option
            fir_design='firwin')

### use EEG channel 1 to test
##eeg1 = dat.to_data_frame("EEG 1")
##
### apply notch filter on 60 Hz and 120 Hz
####notched = notch_filter(eeg1.values, sfreq, np.arange(60, 121, 60)))
##
### apply notch filter only on 60 Hz, default setting of OpenBCI
####notched = notch_filter(eeg1.values, sfreq, 60, filter_length=))
