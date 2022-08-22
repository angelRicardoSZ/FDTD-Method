""" 
Description: Simulation of a plane wave (modeled by a Gaussian pulse) propagating on the z-axis 
            such that the electric field oscillates on the x-axis and 
            the magnetic field on the y-axis. 
Parameters: nz: spatial steps
            nt: temporal steps
            ex: x component of the electric field. Array of length nz
            hy: x component of the magnetic field. Array of length nt
            exWave: x component of the electric field in all time
            hyWave: y component of the magnetic field in all time
            nsource1: node on which the pulse 1 is created
            tsource: time on which the pulse 1 is created
            width1: affects the width of pulse 1 
"""
import numpy as np
from math import exp

import utilities

nz = int(input("Ingresa el número de pasos espaciales, por ejemplo 200 (debe ser un número par): "))

# Validation of nz

nt = int(input("Ingresa el número de pasos temporales, por ejemplo 270 (debe ser un número par): "))

# Validation of nt
print("Parameters of source 1")

spatialOffset1 = int(input("Ingresa el desfase espacial para la onda 1, por ejemplo -20 : "))

temporalOffset1 = int(input("Ingresa el desfase temporal para la onda 1, por ejemplo 40 : "))

bandwidth1= int(input("Ingresa el ancho de banda para la onda 1, por ejemplo 12 : "))

# Creating arrays ex and hy (this array stores the data for each time step temporally)
ex = np.zeros(nz)
hy = np.zeros(nz)

# Creating arrays that stores the data for each time step for all spatial domain
# row t = 0*time_step : z = 0, z = k*1,  z = k*2, ..., z = k*(nz-1)
# row t = 1*time_step : z = 0, z = k*1,  z = k*2, ..., z = k*(nz-1)
# .
# .
# .
# row t = (nt-1)*time_step : z = 0, z = k*1,  z = k*2, ..., z = k*(nz-1)

exWave = np.zeros((nz,nt)) 
hyWave = np.zeros((nz,nt))   

# Wave parameters

# Initial position
nsource1 = int(nz / 2) + spatialOffset1
#nsource2 = int(nx / 2) - 20

# FDTD-1D method
for time_step in range(1, nt + 1):
    # Ex 
    for k in range(1, nz):
        #ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])       # Equation 1.9a from book
        ex[k] = ex[k] + 1 * (hy[k - 1] - hy[k])       # Courant number -> 1
        # Source
        source = exp(-0.5 * ((temporalOffset1 - time_step) / bandwidth1) ** 2)
        ex[nsource1] = source    # Source located at kc - 20
        #ex[nsource2] = source    # Source located at kc + 20             
    # Hy
    for k in range(nz - 1):
        #hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])        # Equation 1.9b from book
        hy[k] = hy[k] + 1 * (ex[k] - ex[k + 1])        # Courant number -> 1
        # source = exp(-0.5 * ((tsource1 - time_step) / width1) ** 2)
        #hy[nsource1] = source
    exWave[:,time_step-1] = ex
    hyWave[:,time_step-1] = hy
    
# Visualization
# automatizar oara cualquier fraccion

t_select = int(((nt-1)/10)*1)
utilities.plot(t_select,exWave,hyWave)

t_select = int(((nt-1)/10)*3)
utilities.plot(t_select,exWave,hyWave)

t_select = int(((nt-1)/10)*5)
utilities.plot(t_select,exWave,hyWave)

t_select = int(((nt-1)/10)*8)
utilities.plot(t_select,exWave,hyWave)

t_select = int(((nt-1)/10)*9)
utilities.plot(t_select,exWave,hyWave)