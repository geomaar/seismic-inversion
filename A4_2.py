""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 4 Problem 2
"""
import matplotlib.pyplot as plt
import math
import numpy as np
from tabulate import tabulate


data = np.loadtxt('Data/velocity_profile.txt')
thickness = data[:, 0]
vel = data[:, 1]
print("The top of the reservoir depth is", sum(thickness))

anglemax = 30*math.pi / 180
Nangles = 100
angles = np.linspace(0, anglemax, Nangles)
P = np.sin(angles) / vel[0]

X = []
T = []

for p in P:
    pV = p*vel
    X.append(sum(2*thickness * pV / np.sqrt(1-pV**2)))
    T.append(sum(2*thickness / vel / np.sqrt(1-pV**2)))

plt.plot(X, T, 'b-')
plt.ylim(2.3, 1.5)
plt.xlabel("Offset(m)")
plt.ylabel("Time (s)")
plt.show()

# RMS velocities
DeltaT = 2*thickness / vel
V2cum = np.cumsum(vel**2 * DeltaT)
Tcum = np.cumsum(DeltaT)
V2rms = V2cum / Tcum
Vrms = np.sqrt(V2rms)
print(tabulate(zip(Tcum, Vrms), headers=["Time", "Vrms"],  tablefmt='orgtbl'))
print()
# Interval velocities using DIX formula
Vint = [Vrms[0]]
for k,v in enumerate(Vrms[1:]):
    Vint.append(np.sqrt((V2rms[k+1]*Tcum[k+1] - V2rms[k]*Tcum[k]) / DeltaT[k+1]))
print(tabulate(zip(DeltaT, Vint), headers=["Time", "Vint"],  tablefmt='orgtbl'))

