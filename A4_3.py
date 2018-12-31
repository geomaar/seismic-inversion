""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 4 Problem 3
"""
import matplotlib.pyplot as plt
import numpy as np
import wavelet as wv

dt = 0.002  # Sampling interval in sec.
center_freq = 25  # Center frequency in Hz.
Nw = 41  # Number of samples in wavelet.
w = wv.ricker(Nw, dt, center_freq)

R0top = 2.05
R0base = 2.15
Nt = 101
r = np.zeros(Nt)  # Make a trace of zero reflection coefficients
r[25] = R0top  # 2.050 s starting from 2.000
r[75] = R0base  # 2.150 s
d = np.convolve(r, w, 'same')  # Convolution returning the central part
t = 2 + np.linspace(0, (Nt-1)*dt, 101)
plt.plot(d, t)
plt.ylim(2.2, 2)
plt.ylabel('Time (s)')
plt.show()
