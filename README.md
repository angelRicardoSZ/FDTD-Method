# FDTD-Method
Simulation of the propagation of electromagnetic waves using the method of finite differences in the time domain (FDTD) based on the work of some authors: 

## Electromagnetic Simulation Using the FDTD method with python, Jennifer E. Houle

Topics:

One-Dimensional Simulation with the FDTD method

**Chapter 1**

In this chapter, a one dimensional simulation is developed. For this end a series of program are created.

**ch_1_1.py**.

In this section a Gaussian pulse is propagated on th z-axis such that the electric field oscillates on the x-axis and the magnetic field on the y-axis, for this, Maxwell´s equations are solved in a vacuum. 
$$
\frac{\partial E_{x}}{\partial t} =- \frac{1}{\epsilon_{0}} \frac{\partial H_{y}}{\partial z} \ \ \ \ \  (eq. 1)
$$

$$
\frac{\partial H_{y}}{\partial t} =- \frac{1}{\mu_{0}} \frac{\partial E_{x}}{\partial z} \ \ \ \ \  (eq. 2)
$$

Using the central difference approximations for the space and time derivatives and using the arrangement showed in Figure 1.1 in the book we get the following equations in an iterative algorithm:
$$
E_{x}^{n+1/2}(k) = 	E_{x}^{n-1/2}(k)-\frac{\Delta t }{\epsilon_{0} \Delta x}[H_{y}^{n}(k+1/2)-H_{y}^{n}(k-1/2)]  \ \ \ (eq.3)
$$
and for the magnetic field
$$
H_{y}^{n+1}(k+1/2) = 	H_{y}^{n}(k+1/2)-\frac{\Delta t }{\mu_{0} \Delta x}[E_{x}^{n+1/2}(k+1)-E_{x}^{n+1/2}(k)]  \ \ \ (eq.4)
$$
Finally we write these last equations on the same scale using the factor
$$
\tilde{E} = \sqrt{\frac{\epsilon_{0}}{\mu_{0}} } E
$$
then the equations 3-4 become: 
$$
\tilde{E}_{x}^{n+1/2}(k) = \tilde{E}_{x}^{n-1/2}(k)-\frac{\Delta t }{\epsilon_{0} \Delta x}[H_{y}^{n}(k+1/2)-H_{y}^{n}(k-1/2)]  \ \ \ (eq.5)
$$
and
$$
H_{y}^{n+1}(k+1/2) = 	H_{y}^{n}(k+1/2)-\frac{\Delta t }{\sqrt{\epsilon_{0} \mu_{0}}  \Delta x}[\tilde{E}_{x}^{n+1/2}(k+1)-\tilde{E}_{x}^{n+1/2}(k)]  \ \ \ (eq.6)
$$
Using
$$
\Delta t = \frac{\Delta x }{2 c_{0}}
$$
we get
$$
\frac{\Delta t }{\sqrt{\epsilon_{0} \mu_{0}} \Delta x} = \frac{\Delta x }{2 c_{0}}  \frac{1} {\sqrt{\epsilon_{0} \mu_{0}} \Delta x}  = 1/2
$$
then equations 5 and 6 are equivalent to the code in python:

```python
ex[k] = ex[k] + 0.5 * (hy[k-1]-hy[k])  (eq.7)
```

and 

```python
hy[k] = hy[k] + 0.5 * (ex[k]-ex[k+1])  (eq.8)
```

Time is implicit in the FDTD method. In equations 7 and 8, right side is the previous value. Position is explicit, the only difference is that k + 1/2 and k - 1/2 is rounded to k and k-1.

The program **ch_1_1.py** use the equations 7, 8 and a Gaussian wave as a source at the center of the computational domain. The pulse propagates away in both directions.

To see this result, first activate the virtual environment 

```bash
.\venv\Scripts\activate
```

then run 

```
py ch_1_1.py
```

Activities

1.- 

