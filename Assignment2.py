""" 
    Maria Antonieta Alcantara Rodriguez
    Fall 2018
    GEO 670
    Assignment 2
"""

# Needed libraries
import matplotlib.pyplot as plt
import math
import numpy as np
import gassmann as gm
from tabulate import tabulate

# Initial data
GPa = 1e9
# Quartz properties:
rho_0 = 2650.0
K_0 = 37.0*GPa
G_0 = 44.0*GPa
# Brine properties:
rho_b = 1025.0
K_b = 2.75*GPa
G_b = 0
#Oil properties:
rho_o = 750.0
K_o = 0.8*GPa
G_o = 0
# Gas properties:
rho_g = 230.0
K_g = 0.1*GPa
G_g = 0

# Problem 2

# Porosity vector
POR = np.linspace(0,1,101) 
# Bulk density for all porosity values :
RHO = POR * rho_b + (1-POR)*rho_0
plt.figure(1)
plt.plot(POR,RHO)
plt.xlabel("Porosity") 
plt.ylabel("Bulk Density")
plt.title("Bulk density as a function of porosity")
plt.axis([0,1,1000,2800])
plt.show()

# Bulk modulus:
KV = POR*K_b + (1-POR)*K_0
KR = (POR/K_b + (1-POR)/K_0)**(-1)
KH = 0.5*(KV+KR)
plt.figure()
plt.plot(POR,KV,'r--',POR,KR,'bs',POR,KH,'g^')
plt.xlabel("Porosity")
plt.ylabel("Bulk Modulus")
plt.axis([0,1,0,40000000000])
plt.show()
# Shear modulus:
GV = POR*G_b + (1-POR)*G_0
GR = (POR/G_b + (1-POR)/G_0)**(-1)
GH = 0.5*(GV+GR)
plt.figure()
plt.plot(POR,GV, 'r--',POR,GR,'bs',POR,GH,'g^')
plt.xlabel("Porosity") 
plt.ylabel("Shear Modulus")
plt.axis([0,1,0,45000000000])
plt.show()

# VP:
VP_V = np.sqrt( np.divide (KV+4/3*GV,  RHO) )
VP_R = np.sqrt( np.divide (KR+4/3*GR,  RHO) )
VP_H = np.sqrt( np.divide (KH+4/3*GH,  RHO) )
plt.figure()
plt.plot(POR,VP_V,'r--',POR,VP_R, 'bs',POR,VP_H,'g^')
plt.xlabel("Porosity")
plt.ylabel("P-wave Velocity")
plt.axis([0,1,1000,7000])
plt.show()

# VS:
VS_V = np.sqrt( np.divide(GV, RHO) )
VS_R = np.sqrt( np.divide(GR, RHO) )
VS_H = np.sqrt( np.divide(GH, RHO) )
plt.figure()
plt.plot(POR,VS_V,'r--', POR,VS_R, 'bs', POR,VS_H,'g^')
plt.xlabel("Porosity")
plt.ylabel("S-wave Velocity")
plt.axis([0,1,0,4500])
plt.show()

# Problem 3

por = 0.3
# Log measurements in oil saturated reservoir:
Vp_OilSat = 3050
Vs_OilSat = 1660

# Bulk density oil sat:
Rho_OilSat = por*rho_o + (1-por)*rho_0
AI_OilSat = Rho_OilSat*Vp_OilSat

# Oil saturated moduli:
G_OilSat = Rho_OilSat * Vs_OilSat**2
K_OilSat = Rho_OilSat * Vp_OilSat**2 -4/3*G_OilSat

# Dry sandstone frame modulus:
K_dry = gm.gassmanninv(K_0, K_OilSat ,K_o, por)
G_dry = G_OilSat

# Substitution to brine:
Rho_BrineSat = por*rho_b + (1-por)*rho_0
K_BrineSat = gm.gassmann(K_0,K_dry,K_b,por)
G_BrineSat = G_dry
M_BrineSat = K_BrineSat + 4/3*G_BrineSat
Vs_BrineSat = math.sqrt( G_BrineSat / Rho_BrineSat )
Vp_BrineSat = math.sqrt( M_BrineSat / Rho_BrineSat )
AI_BrineSat = Rho_BrineSat*Vp_BrineSat

# Substitution to gas:
Rho_GasSat = por*rho_g + (1-por)*rho_0
K_GasSat = gm.gassmann(K_0,K_dry,K_g,por)
G_GasSat = G_dry
M_GasSat = K_GasSat + 4/3*G_GasSat
Vs_GasSat = math.sqrt( G_GasSat / Rho_GasSat )
Vp_GasSat = math.sqrt( M_GasSat / Rho_GasSat )
AI_GasSat = Rho_GasSat*Vp_GasSat


print (tabulate([['Brine', Rho_BrineSat, Vp_BrineSat, Vs_BrineSat, AI_BrineSat, Vp_BrineSat/Vs_BrineSat],
                 ['Oil', Rho_OilSat, Vp_OilSat, Vs_OilSat, AI_OilSat, Vp_OilSat/Vs_OilSat],
                 ['Gas', Rho_GasSat, Vp_GasSat, Vs_GasSat, AI_GasSat, Vp_GasSat/Vs_GasSat]],
                headers=["Case","Rho", "Vp", "Vs", "AI", "Vp/Vs"],  tablefmt='orgtbl'))
