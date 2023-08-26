# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:26:18 2022

@author: Lakshya Singh
"""

import sympy as sp
#from sympy import *
#import numpy as np
from sympy.matrices import zeros
from pprint import pprint

x,y,z,rho,a,m = sp.symbols("x,y,z,rho,a,m")

a = 1
m = 1

rho = m/(a**3)

#I = sp.Array([[0,0,0]]*3)
I = zeros(3,3)


for i in range(3):
    for j in range(3):
        if (i==j):
            I[i,j] = rho*sp.integrate(y**2+z**2,(x,0,a),(y,0,a),(z,0,a))
        else:
            I[i,j] = -rho*sp.integrate(y*z,(x,0,a),(y,0,a),(z,0,a))

print("Moment of inertia tensor: ")
pprint(I)
print()
v1,v2,v3 = I.eigenvects()
print("Principal moments are: ",v1[0],v2[0],v3[0])
print()
print("Principal axes are: ")
pprint(v1[2])
print()
pprint(v2[2])
print()
pprint(v3[2])





