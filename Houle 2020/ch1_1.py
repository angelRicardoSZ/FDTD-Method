""" 
Description: Simulation of a plane wave (modeled by a Gaussian pulse) propagating on the z-axis 
            such that the electric field oscillates on the x-axis and 
            the magnetic field on the y-axis. 
Parameters: nx: spatial steps
            nt: temporal steps
            ex: x component of the electric field
            hy: x component of the electric field
            nsource1: node on which the pulse 1 is created
            tsource: time on which the pulse 1 is created
            width1: affects the width of pulse 1 
"""
import numpy as np
from math import exp
from matplotlib import pyplot as plt

nx = 200
nt = 100
ex = np.zeros(nx)
hy = np.zeros(nx)

# Wave parameters
nsource1 = int(nx / 2)
tsource1 = 40
width1 = 12

# FDTD-1D method
for time_step in range(1, nt + 1):
    # Ex 
    for k in range(1, nx):
        ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])       # Equation 1.9a from book
        # Source
        source = exp(-0.5 * ((tsource1 - time_step) / width1) ** 2)
        ex[nsource1] = source
        
    # Hy
    for k in range(nx - 1):
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])        # Equation 1.9b from book

# Graphics
plt.rcParams['font.size'] = 12
plt.figure(figsize=(8, 3.5))

plt.subplot(211)
plt.plot(ex, color='k', linewidth=1)
plt.ylabel('E$_x$', fontsize='14')
plt.xticks(np.arange(0, 201, step=20))
plt.xlim(0, 200)
plt.yticks(np.arange(-1, 1.2, step=1))
plt.ylim(-1.2, 1.2)
plt.text(100, 0.5, 'T = {}'.format(time_step),horizontalalignment='center')

plt.subplot(212)
plt.plot(hy, color='k', linewidth=1)
plt.ylabel('H$_y$', fontsize='14')
plt.xlabel('FDTD cells')
plt.xticks(np.arange(0, 201, step=20))
plt.xlim(0, 200)
plt.yticks(np.arange(-1, 1.2, step=1))
plt.ylim(-1.2, 1.2)
plt.subplots_adjust(bottom=0.2, hspace=0.45)
plt.show()