# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:22:12 2019
Last edit on Wed Jun 26 11:47:12 2019

@author: Julian, Yiwen
"""
from sys import argv
import numpy as np
import mne

class converter:
    def __init__(self, name):
        self.name = name
        self.raw = None
        
    def convert(self, chs=list(range(1, 9)), drop_empty=True):
        # Assume under same folder, and input text using OpenBCI format
        # Directlt use the file, `chs` is a list of channel used
        # In default setting, all 8 channels are kept, except all empty channels
        
        # Read the CSV file as a NumPy array
        data = np.loadtxt(self.name, delimiter=",", skiprows=6, usecols=tuple(chs))
        
        # Drop empty channels
        nonzeros = np.where(~np.all(data==0, axis=0))[0]
        data = data[:, nonzeros]
        
        # Some information about the channels
        ch_names = [f"EEG{i}" for i in range(1, data.shape[-1]+1)]
        
        # Sampling rate of the Cyton Board
        sfreq = 250 # Hz
        
        # Create the info structure needed by MNE
        info = mne.create_info(ch_names, sfreq)

<<<<<<< HEAD
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
||||||| merged common ancestors
# Read the CSV file as a NumPy array
data = np.loadtxt(name[-1], delimiter=',', skiprows=6, usecols=tuple(range(1,9)))

# Some information about the channels
ch_names = ['CH 1','CH 2','CH 3','CH 4','CH 5','CH 6','CH 7','CH 8']  

# Sampling rate of the Cyton Board
sfreq = 250  # Hz

# Create the info structure needed by MNE
info = mne.create_info(ch_names, sfreq)

# Finally, create the Raw object and save
raw = mne.io.RawArray(data.T, info)
raw.save(f"{name[-1].split('.')[0]}.fif")
=======
        # Create the Raw object
        self.raw = mne.io.RawArray(data.T, info)
        
        # Add channels
        for n in ch_names:
            self.raw.set_channel_types(mapping={f"{n}": "eeg"})
            
        return self.raw
        
    def save(self):
        if self.raw is None:
            self.convert()
        # Save converted file
        self.raw.save(f"{self.name.split('.')[0]}.fif")
        
if __name__ == "__main__":
    # Pass .txt data from openbci gui as argument
    name = argv
    if len(name) == 2:
        name = name[-1]
    else:
        raise AttributeError("Number of arguments is invalid, received arguments: {name}")
    c = converter(name)
    c.save()
>>>>>>> refs/remotes/origin/master
