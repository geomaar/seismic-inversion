""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 1 - Problem 4
"""

# Initial data
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
import numpy as np
from tabulate import tabulate

fig, ax = plt.subplots()
GPa = 1e9           # Define Giga Pascal
K = 16.0*GPa        # Set bulk modulus
G = 7.0*GPa         # Set shear modulus
nu = (3*K-2*G) / (2*(3*K+G)) # Calculate Poisson's ratio
rho = 2150          # Define density in kg/m^3
M = K + 4/3*G       # Calculate compressional modulus
Vp = math.sqrt(M/rho)    # Calculate P-wave velocity
Vs = math.sqrt(G/rho)    # Calculate S-wave velocity
f = 30              # Set frequency
T = 1/f             # Calculate the period
omega = 2*math.pi*f      # Calculate the angular frequency
lbd = Vp * T        # Calculate the wave-length
k = 2*math.pi / lbd      # Calculate the wave-number

print(tabulate ([["Poisson's ratio", nu ],
                ["Compressional modulus", M/1000000000,"GPa"],
                ["P-wave velocity ", Vp, "m/s"],
                ["S-wave velocity", Vs,"m/s"],
                ["Period", T, "s"],
                ["Angular frequency", omega],
                ["Wavelength", lbd, "m/s"],
                ["Wave number ", k, "1/m"]],
                tablefmt='orgtbl'))
x = 1000
T = np.linspace(0, 0.1, 101)
u = np.exp(1j * (k * x - omega * T))
plt.figure(1)
plt.plot(T,u)
plt.axis([0,0.1,-1,1])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Wave at x=1000m")
plt.show()
