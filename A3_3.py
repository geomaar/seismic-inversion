""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 3 Problem 3
"""

#Needed libraries
import matplotlib.pyplot as plt
import math
import numpy as np

A = 0.5 
freq = 50
Nt = 1000   # Length of signal
dt = 0.001  # Sampling interval (sec.)
t = np.linspace(0,(Nt-1)*dt,501) # Time vector
m = Nt/2+1
fnq = 1/(2*dt) # Nyquist frequency
f = np.linspace(0,fnq,m) # % Frequency vector
# Signal
s = A*np.sin(2*math.pi*freq*t)
plt.figure()
plt.plot(1000*t,s)
plt.title("Harmonic Signal")
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.show()

fourier = np.fft.fft(s)
plt.figure()
plt.plot(f,fourier)
plt.title("Amplitude spectrum")
plt.xlabel('Frequency HZ')
plt.ylabel('Amplitude')
plt.show()
