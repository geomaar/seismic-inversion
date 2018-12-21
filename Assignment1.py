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

"""
plt.figure(2)
X= np.linspace(-300,300, 601)
t = 0
u = np.exp(1j*(k*X-omega*t))
plt.plot(X,u)
plt.axis([-300,300,-1,1])
plt.title("Wave at t=0")
plt.xlabel("Distance (m)")
plt.ylabel("Amplitude")
plt.show()
"""
# second figure
X = np.arange(-300, 300, 1)
t = 0
u = np.exp((k * X - omega * t) * 1j)

line, = ax.plot(X, u)

def animate(t):
    line.set_ydata(np.exp((k * X - omega * t) * 1j))
    return line,

def init():
    line.set_ydata(np.ma.array(X, mask=True))
    return line,

ani = animation.FuncAnimation(
    fig, animate, np.arange(1, 100, 0.001),
    init_func=init,
    interval=25,
    blit=True)

plt.title('title!!!')
plt.xlabel('distance (m)')
plt.ylabel('amplitude')
plt.show()
