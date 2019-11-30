# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

fs, data = read("dolphinsound_20_sec.wav")
ch1 = data[:,0]
ch1 = ch1-np.mean(ch1)

tstart = 15
tend = 18
signal_choose = ch1[tstart*fs:tend*fs]
t = np.arange(tstart, tend, 1/fs)

nperseg = 1024
f, t, Zxx = stft(signal_choose, nperseg=nperseg, window='hann', fs=fs, noverlap=nperseg*0.5, nfft=nperseg, boundary=None, padded=False)
a = np.abs(Zxx)
f_down = 40
f_index = 81
energy_cut = np.sum(a[f_down:f_index, :], axis=0)

fg, (ax1, ax2) = plt.subplots(2, 1, sharex='row')
fg.set_size_inches(6.4*4, 4.8*4)
cmap = plt.get_cmap('gist_heat')
ax1.axhline(5625 , color='r', ls='--')
ax1.axhline(6562.5 , color='r', ls='--')
# ax1.axvline( , color='r', ls='--')
ax1.pcolormesh(t, f[:100], a[:100, :], cmap=cmap, vmin=0, vmax=80)

ax2.plot(t, energy_cut)