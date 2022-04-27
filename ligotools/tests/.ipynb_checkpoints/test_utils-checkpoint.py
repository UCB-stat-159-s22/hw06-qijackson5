import numpy as np
import pytest
from ligotools import utils 
from ligotools import readligo as rl
import matplotlib.mlab as mlab



def test_whiten_H1():
    fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    whiten_data = 1
    fs = 4096
    NFFT = 16384
    dt = 0.000244140625
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    psd_H1 = interp1d(freqs, Pxx_H1)
    strain_H1_whiten = whiten(strain_H1,psd_H1,dt) 
    actual_strain_H1_whiten = 131072
    assert(len(strain_H1_whiten == actual_strain_H1_whiten))
    
def test_whiten_L1():
    fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    whiten_data = 1
    fs = 4096
    NFFT = 16384
    dt = 0.000244140625
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
    Pxx_L1, freqs = mlab.psd(strain_L1, Fs = fs, NFFT = NFFT)
    psd_L1 = interp1d(freqs, Pxx_L1)
    strain_L1_whiten = whiten(strain_L1,psd_L1,dt)
    actual_strain_L1_whiten = 131072
    assert(len(strain_L1_whiten == actual_strain_L1_whiten))
    

# test to make sure that reqshift doesnt change the size for whiten H1
def test_reqshift_H1():
    fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    whiten_data = 1
    fs = 4096
    NFFT = 16384
    dt = 0.000244140625
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    psd_H1 = interp1d(freqs, Pxx_H1)
    strain_H1_whiten = whiten(strain_H1,psd_H1,dt) 
    strain_H1_shifted = reqshift(strain_H1_whitenbp,fshift=fshift,sample_rate=fs)
    assert(len(strain_H1_whiten) == len(strain_H1_shifted)) 
    
# test to make sure that reqshift doesnt change the size for whiten L1
def test_reqshift_L1():
    fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    whiten_data = 1
    fs = 4096
    NFFT = 16384
    dt = 0.000244140625
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
    Pxx_L1, freqs = mlab.psd(strain_L1, Fs = fs, NFFT = NFFT)
    psd_L1 = interp1d(freqs, Pxx_L1)
    strain_L1_whiten = whiten(strain_L1,psd_L1,dt)
    strain_L1_shifted = reqshift(strain_L1_whitenbp,fshift=fshift,sample_rate=fs)
    assert(len(strain_L1_whiten) == len(strain_L1_shifted))