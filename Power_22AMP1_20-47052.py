# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 06:12:53 2022

@author: Lakshya Singh
"""

#power method
import numpy as np

#A = np.array(([2,-12],[1,-5]))
#A = np.array(([1,-3,3],[3,-5,3],[6,-6,4]))
A = np.array(([2,-3],[1,-5]))
#A = np.array(([5,4],[1,2]))
#A = np.array(([-2,4],[1,2]))


# for direct power mthod use the following syntax

#B = A  

# for inverse power method open the following syntax

B = np.linalg.inv(A)

x = np.array(([1],[1]))
#x = np.array(([1],[1],[1]))


e = 1e-5
k = 0

eig1 = max(x)

#norm = np.linalg.norm
#norm = max

for i in range(50):
    k = k+1
    x = np.dot(B,x)
    #print(x)
    eig2 = max(x)
    x = x/eig2
    print("Iteration: ",k)
    print("------------------------------------------")
    #print(x)
    print("Dominant Eigenvalue: ",eig2)   

    print("Eigenvector: ",x)
    
    print()
    print()
    if (abs(eig1-eig2) <= e):
        break
    eig1 = eig2
  

print()

print("Using inbuilt command the eigenvalues and eigenvector of A are: ",(np.linalg.eig(A)))
    































































"""
k = 0
for i in range(1000):
    k = k+1
    x_new = np.dot(A,x)
    val = max((x_new))
    p = x_new/val
    if(abs((p)[0] - (x)[0]) <= e):
        break
    else:
        x = x_new/val
    print("Iteration: ",k)
    print(val)
    print(x)
    print()
    
#p1 = np.dot(A,x)
#p2 = p1/norm(p1)
#while (abs(p2[0]-p1[0]) > e):  
"""   



