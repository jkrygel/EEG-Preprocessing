# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:22:12 2019

@author: Yiwen, Julian

The code converts OpenBCI text data to raw fif data
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
