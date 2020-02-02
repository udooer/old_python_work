#!/usr/bin/env python



import numpy as np
import soundfile as sf

dur = float(input("Get duration(second): "))
f0 = float(input("Get the base frequency(Hz): "))
fe = float(input("Get the end frequency(Hz): "))
filename = str(input("Enter the filename: "))
filename = "./" + filename + ".wav"

fs = 96000
Amp = 1

t = np.linspace(0, dur, fs*dur+1)
mu = (fe-f0)/(2*dur)
signal = Amp*np.cos(2*np.pi*(f0*t+mu*t*t))
sf.write(filename, signal, fs, 'PCM_24')
