# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 7:51:25 2019

@author: Yiwen, Julian

The code is about notch filter, bandpass filter and fft
"""
import mne.filter as mf
import numpy as np
from numpy.fft import fft

class filters:
    @staticmethod
    def notch_filter(dat, Fs=250, freqs=60):
        # apply notch filter only on 60 Hz, default setting of OpenBCI
        # sampling rate is 250 Hz
        # `dat` is an array
        # https://www.martinos.org/mne/stable/generated/mne.filter.notch_filter.html
        # `notch_filter` can be a class method in data
        # https://www.martinos.org/mne/stable/generated/mne.io.RawArray.html?highlight=notch_filter#mne.io.RawArray.notch_filter
        # e.g.: dat.notch_filter(60)
        return mf.notch_filter(dat, Fs, freqs)

    @staticmethod
    def bandpass_filter(dat, l_freq, h_freq, sfreq=250):
        # apply bandpass filter on data
        # sampling rate is 250 Hz
        # `dat` is an array
        # https://www.martinos.org/mne/stable/generated/mne.filter.filter_data.html
        # this is no longer used: https://mne-tools.github.io/0.13/generated/mne.filter.band_pass_filter.html
        # e.g.: a class method in data: bandpass filter (Beta)
        # dat.filter(13, 25, n_jobs=1,        # use more jobs to speed up
        #             l_trans_bandwidth=1,    # make sure filter params are the same
        #             h_trans_bandwidth=1,    # in each band and skip "auto" option
        #             fir_design="firwin")
        return mf.filter_data(dat, sfreq, l_freq, h_freq, l_trans_bandwidth=1, h_trans_bandwidth=1, n_jobs=1, fir_design="firwin")

##    @staticmethod
##    def fft(dat):
##        r = fft(dat).real
##        return np.log10(np.clip(r, 1e-20, 1e100))

    @staticmethod
    def fft(dat):
        Fs = 250 # sample rate
        T = 1 / Fs # sampling period
        t = 0.004 # seconds of sampling
        N = Fs * t # total points in signal
        y = fft(y)[0: int(N / 2)] / N
        y[1:] = 2 * y[1:]
        y = abs(y)
        f = Fs * np.arange((N / 2)) / N
        return f, y
