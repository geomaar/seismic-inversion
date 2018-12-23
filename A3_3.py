""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 3 Problem 3
"""

# Needed libraries
import matplotlib.pyplot as plt
import math
import numpy as np

A = 0.5
freq = 50
Nt = 1000   # Length of signal
dt = 0.001  # Sampling interval (sec.)
t = np.linspace(0, (Nt-1)*dt,501)  # Time vector
m = Nt/2+1
fnq = 1/(2*dt)  # Nyquist frequency
f = np.linspace(0, fnq, m)  # % Frequency vector
# Signal
s = A*np.sin(2*math.pi*freq*t)
plt.figure()
plt.plot(1000*t, s)
plt.title("Harmonic Signal")
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.show()

fourier = np.fft.fft(s) # Fourier transform
plt.figure()
plt.plot(f, fourier)
plt.title('Single-Sided Amplitude Spectrum')
plt.xlabel('Frequency HZ')
plt.ylabel('Amplitude')
plt.show()

# Sum of two harmonic signals
suma = A*np.sin(2*math.pi*freq*t)+0.7*np.sin(2*math.pi*80*t)
plt.figure()
plt.plot(1000*t, suma)
plt.title("Sum of two harmonic signals")
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.axis([0,150,-1.5,1.5])
plt.show()

fourier2 = np.fft.fft(suma) # Fourier transform
plt.figure()
plt.plot(f, fourier2)
plt.title('Single-Sided Amplitude Spectrum')
plt.xlabel('Frequency HZ')
plt.ylabel('Amplitude')
plt.show()