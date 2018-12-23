""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 2 Problem 6
"""

#Needed libraries
import matplotlib.pyplot as plt
import math
import numpy as np
import gassmann as gm
from tabulate import tabulate

#Define GigaPascal
GPa = 1e9

# Quartz:
rho_q = 2650.0
K_q = 37.0*GPa
G_q = 44.0*GPa

# Clay:
rho_c = 2600.0
K_c = 30.0*GPa
G_c = 10.0*GPa

# Brine:
rho_b = 1025.0
K_b = 2.75*GPa
G_b = 0

# Oil:
rho_o = 750.0
K_o = 0.8*GPa
G_o = 0

# Gas:
rho_g = 230.0
K_g = 0.1*GPa
G_g = 0

C = 0.2     # Relative fraction clay
KR = ( C/K_c + (1-C)/K_q )**-1  # Reuss
KV = C*K_c + (1-C)*K_q          # Voigt
K0 = 0.5*(KR+KV)                # Hill
GR = ( C/G_c + (1-C)/G_q )**-1  # Reuss
GV = C*G_c + (1-C)*G_q          # Voigt
G0 = 0.5*(GR+GV)                # Hill

rho_0 = C*rho_c + (1-C)*rho_q   # Mineral density

POR = np.linspace(0.1, 0.35, 100)
por_c = 0.4
K_dry = K0*(1-POR/por_c)
G_dry = G0*(1-POR/por_c)
K = gm.gassmann(K0,K_dry,K_b,POR) # Brine saturated bulk mod.
G = G_dry
M = K + 4/3*G
RHO = POR*rho_b + (1-POR)*rho_0
VP = np.sqrt(np.divide(M,RHO))
VS = np.sqrt(np.divide(G,RHO))
AI = VP*RHO
VPVS = np.divide(VP,VS)
plt.figure()
plt.plot(AI,VPVS,'b*')
plt.show()