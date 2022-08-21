# FDTD-Method
Simulation of the propagation of electromagnetic waves using the method of finite differences in the time domain (FDTD) based on the work of some authors: 

## Electromagnetic Simulation Using the FDTD method with python, Jennifer E. Houle

Topics:

One-Dimensional Simulation with the FDTD method

**Chapter 1**

In this chapter, a one dimensional simulation is developed. For this end a series of program are created.

**ch_1_1.py**.

In this section a Gaussian pulse is propagated on th z-axis such that the electric field oscillates on the x-axis and the magnetic field on the y-axis, for this, Maxwell´s equations are solved in a vaccum. 
$$
\frac{\partial E_{x}}{\partial t} =- \frac{1}{\epsilon_{0}} \frac{\partial H_{y}}{\partial z} \ \ \ \ \  (eq. 1)
$$

$$
\frac{\partial H_{y}}{\partial t} =- \frac{1}{\mu_{0}} \frac{\partial E_{x}}{\partial z} \ \ \ \ \  (eq. 2)
$$

Using the central difference approximations for the space and time derivatives and using the following arrangement

![](D:\Software development\FDTD-Method\Houle 2020\ch1_1_1.png)









