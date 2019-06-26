# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:22:12 2019

@author: Julian
"""
from sys import argv
import numpy as np
import mne

# Pass .txt data from openbci gui as argument
name = argv

# Read the CSV file as a NumPy array
data = np.loadtxt(name[-1], delimiter=',', skiprows=6, usecols=tuple(range(1,9)))

# Some information about the channels
ch_names = ['EEG1','EEG2','EEG3','EEG4','EEG5','EEG6','EEG7','EEG8']  

# Sampling rate of the Cyton Board
sfreq = 250  # Hz

# Create the info structure needed by MNE
info = mne.create_info(ch_names, sfreq)

# Finally, create the Raw object and save
raw = mne.io.RawArray(data.T, info)
raw.save(f"{name[-1].split('.')[0]}.fif")