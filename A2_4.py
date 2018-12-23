""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 2 Problem 4
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
print("K_dry = ",K_dry/1e9,"GPa")
print("G_dry = ", G_dry/1e9, "GPa")

Sw = 0.2    # Water saturation
rho_f = Sw*rho_b + (1-Sw)*rho_o     # Oil-brine fluid density
K_f = ( Sw/K_b + (1-Sw)/K_o )**(-1) # Oil-brine bulk modulus
Rho_OilSat = por*rho_f + (1-por)*rho_0  # Bulk density
K_OilSat = gm.gassmann(K0,K_dry,K_f,por)#  Saturated bulk modulus
G_OilSat = G_dry    # Saturated shear modulus
M_OilSat = K_OilSat + 4/3*G_OilSat  # Saturated compressional modulus
Vs_OilSat = math.sqrt( G_OilSat / Rho_OilSat )  # Vs
Vp_OilSat = math.sqrt( M_OilSat / Rho_OilSat )  # Vp
AI_OilSat = Rho_OilSat*Vp_OilSat                # Acoustic impedance

print(tabulate ([["Original gas", Rho , Vp_log, Vs_log, Rho*Vp_log, Vp_log/Vs_log ],
                ["Subst. Oil", Rho_OilSat, Vp_OilSat, Vs_OilSat, AI_OilSat,Vp_OilSat/Vs_OilSat]],
                headers=["Case","Rho", "Vp", "Vs", "AI", "Vp/Vs"], tablefmt='orgtbl'))