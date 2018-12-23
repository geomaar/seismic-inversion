""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 2 Problem 5
"""

#Needed libraries
import matplotlib.pyplot as plt
import math
import numpy as np
import gassmann as gm
from tabulate import tabulate

# Initial data
por = 0.3   # Porosity
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

# Water and gas saturation
Sw = 0.2
Sg = 0.8 
rho_f = Sw*rho_b + Sg*rho_g
K_f = ( Sw/K_b + Sg/K_g )**(-1)

C = 0.2     # Relative fraction clay
KR = ( C/K_c + (1-C)/K_q )**-1  # Reuss
KV = C*K_c + (1-C)*K_q          # Voigt
K0 = 0.5*(KR+KV)                # Hill
GR = ( C/G_c + (1-C)/G_q )**-1  # Reuss
GV = C*G_c + (1-C)*G_q          # Voigt
G0 = 0.5*(GR+GV)                # Hill

rho_0 = C*rho_c + (1-C)*rho_q   # Mineral density
Rho = por*rho_f + (1-por)*rho_0 # Saturated rock density

Vp_log = 3040 
Vs_log = 1670
G = Rho * Vs_log**2             # Gas saturated shear modulus
K = Rho * Vp_log**2 - 4/3*G     # Gas saturated bulk from the given modulus

K_dry = gm.gassmanninv(K0, K ,K_f, por)
G_dry = G

""" Problem 5, same reservoir as last problem """

SW = np.linspace(0,1,101)
# Fluid density vector for different saturations:
Rho_f = SW*rho_b + (1-SW)*rho_g
# Bulk density for different saturations:
RHO = por*Rho_f + (1-por)*rho_0
# Bulk modulus complete mix (Reuss):
K_f = ( np.divide(SW,K_b) + np.divide(1-SW,K_g ))**-1

K = gm.gassmann(K0,K_dry,K_f,por)
G = G_dry
M = K + 4/3*G
VP = np.sqrt(np.divide(M, RHO))
VS = np.sqrt(np.divide(G, RHO))
AI = VP*RHO
VPVS = np.divide(VP, VS)

plt.figure()
plt.subplot(231)
plt.plot(SW,RHO)
plt.xlabel('Water saturation')
plt.ylabel('Density')

plt.subplot(232)
plt.plot(SW,VP)
plt.xlabel('Water saturation')
plt.ylabel('Vp')

plt.subplot(233)
plt.plot(SW,VS)
plt.xlabel('Water saturation')
plt.ylabel('Vs')

plt.subplot(234)
plt.plot(SW,AI)
plt.xlabel('Water saturation')
plt.ylabel('Acoustic impedance')

plt.subplot(2,3,5)
plt.plot(SW,VPVS)
plt.xlabel('Water saturation')
plt.ylabel('VP/Vs')

plt.subplot(236)
plt.plot(AI,VPVS,'*')
plt.xlabel('Acoustic impedance')
plt.ylabel('VP/Vs')
plt.show()

# Brine patch:
K_Pb = gm.gassmann(K0,K_dry,K_b,por)
M_Pb = K_Pb + 4/3*G
# Gas patch:
K_Pg = gm.gassmann(K0,K_dry,K_g,por)
M_Pg = K_Pg + 4/3*G
# Hill exact agerage for the compressional modulus:
M = ( np.divide(SW,M_Pb) + np.divide(1-SW,M_Pg ))**-1
K = M - 4/3*G
VP2 = np.sqrt(np.divide(M,RHO))
VS2 = np.sqrt(np.divide(G,RHO))
AI2 = VP2*RHO
VPVS2 = np.divide(VP2,VS2)

# New plots including patchy saturation
plt.figure()
plt.subplot(231)
plt.plot(SW,RHO, 'b--' )
plt.xlabel('Water saturation')
plt.ylabel('Density')

plt.subplot(232)
plt.plot(SW,VP,'b--', SW,VP2, 'r-')
plt.xlabel('Water saturation')
plt.ylabel('Vp')

plt.subplot(233)
plt.plot(SW,VS, 'b--', SW, VS2, 'r-')
plt.xlabel('Water saturation')
plt.ylabel('Vs')

plt.subplot(234)
plt.plot(SW,AI, 'b--', SW, AI2, 'r-')
plt.xlabel('Water saturation')
plt.ylabel('Acoustic impedance')

plt.subplot(2,3,5)
plt.plot(SW,VPVS, 'b--', SW, VPVS2, 'r-')
plt.xlabel('Water saturation')
plt.ylabel('VP/Vs')

plt.subplot(236)
plt.plot(AI,VPVS,'b--', AI2, VPVS2, 'r-')
plt.xlabel('Acoustic impedance')
plt.ylabel('VP/Vs')
plt.show()