""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 4 Problem 2
"""
import matplotlib.pyplot as plt
import math
import numpy as np


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

