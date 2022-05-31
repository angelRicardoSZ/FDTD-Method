""" 
Description: Simulation of a plane wave (modeled by a Gaussian pulse) propagating on the z-axis 
            such that the electric field oscillates on the x-axis and 
            the magnetic field on the y-axis with Absorbing Boundary Condition. 
Parameters: nx: spatial steps
            nt: temporal steps
            ex: x component of the electric field
            hy: x component of the magnetic field
            exWave: x component of the electric field in all time
            hyWave: y component of the magnetic field in all time
            nsource: node on which the pulse is created
            tsource: time on which the pulse is created
            width1: affects the width of pulse 1 
"""
import numpy as np
from math import exp
from matplotlib import pyplot as plt

nx = 200
nt = 270
ex = np.zeros(nx)
hy = np.zeros(nx)
exWave = np.zeros((nx,nt)) 
hyWave = np.zeros((nx,nt))   
# Wave parameters
nsource = int(nx / 2)

tsource = 40
width = 12

boundary_low = [0, 0]
boundary_high = [0, 0]



# FDTD-1D method
for time_step in range(1, nt + 1):
    # Ex 
    for k in range(1, nx):
        #ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])       # Equation 1.9a from book
        ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])       # Courant number -> 1
    # Source
    source = exp(-0.5 * ((tsource - time_step) / width) ** 2)
    ex[nsource] = source    # Source located at kc - 20
        #ex[nsource2] = source    # Source located at kc + 20    
        
    # Absorbing boundary conditions
    ex[0] = boundary_low.pop(0)
    boundary_low.append(ex[1])
    
    ex[nx - 1] = boundary_high.pop(0)
    boundary_high.append(ex[nx - 2])
    # Hy
    for k in range(nx - 1):
        #hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])        # Equation 1.9b from book
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])        # Courant number -> 1
        # source = exp(-0.5 * ((tsource1 - time_step) / width1) ** 2)
        #hy[nsource1] = source
    exWave[:,time_step-1] = ex
    hyWave[:,time_step-1] = hy


#plt.plot(np.arange(0, 200, step=1),exWave[:,250])    


