# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 05:57:01 2022

@author: Lakshya Singh
"""

#strain tensor
import sympy as sp
from sympy.matrices import Matrix,zeros
from pprint import pprint

x,y,z,h1,h2,h3 = sp.symbols("x,y,z,h1,h2,h3")

H = Matrix((h1,h2,h3))
P = Matrix((x,y,z))

def funct1():
    return x*y*z

def funct2():
    return y

def funct3():
    return x*z

fi = [funct1(),funct2(),funct3()]

sym = zeros(3,3)
for i in range(3):
    for j in range(3):
        sym[i,j] += sp.diff(fi[i],P[j])+sp.diff(fi[j],P[i])
        
antisym = zeros(3,3)   
for i in range(3):
    for j in range(3):
        antisym[i,j] += sp.diff(fi[i],P[j])-sp.diff(fi[j],P[i])     
        
print("Symmwtric part of strain: ") 
pprint(sym) 
    
print()
print("Anti-symmwtric part of strain: ")   
pprint(antisym)

strain = zeros(3,3)

for i in range(3):
    for j in range(3):
        strain[i,j] = (1/2)*H[i]*(sym[i,j] + antisym[i,j])

print()
print("Strain tensor: ")
pprint(strain)    


