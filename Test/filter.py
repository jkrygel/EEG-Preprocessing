# -*- coding: utf-8 -*-

import numpy as np
import mne
from mne.filter import notch_filter

# raw data
dat = mne.read_raw_bdf("../Data/Subject_1-1.bdf", preload=True)
event = mne.events_from_annotations(dat)
info = dat.info
sfreq = info.get("sfreq")

# drop accelerometer channels
dat.drop_channels(["Accel X", "Accel Y", "Accel Z"])

# apply notch filter only on 60 Hz, default setting of OpenBCI
# https://martinos.org/mne/stable/generated/mne.io.Raw.html?highlight=notch#mne.io.Raw.notch_filter
dat.notch_filter(60)

# bandpass filter (Beta)
dat.filter(13, 25, n_jobs=1,        # use more jobs to speed up
            l_trans_bandwidth=1,    # make sure filter params are the same
            h_trans_bandwidth=1,    # in each band and skip "auto" option
            fir_design="firwin")

<<<<<<< HEAD
dat.plot()
||||||| merged common ancestors
dat.plot()
>>>>>>> ccc01bf955a20b2ab9051f0a825f8de9e75a87c9
=======
dat.plot()
>>>>>>> refs/remotes/origin/master
