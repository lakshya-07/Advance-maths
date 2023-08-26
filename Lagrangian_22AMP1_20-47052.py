# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 05:49:28 2022

@author: Lakshya Singh
"""



#  oscillating pendulum euler method + odeint
# langragian mechanics

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


a = np.pi/4 #angular displacement

   
ti = 0.0
x = a
v = 0
tf = 5
h = 0.001 


#defining functions
def funct1(x,v,t):
    return v 

def funct2(x,v,t):
    g = 9.8
    l = 0.5
    return (-g/l)*(np.sin(x))

def du_dx(u,t): 
    #for odeint
    # here u[0]=x,u[1]=v
    return [u[1],funct2(u[0],v,ti)]

uo = [x,v]
t_ode = np.linspace(ti,tf,200)
uf = odeint(du_dx,uo,t_ode)
x_ode = uf[:,0]
v_ode = uf[:,1]

accl_ode = [funct2(x_ode[i],v_ode[i],t_ode[i]) for i in range(1,len(t_ode))]
accl_ode.insert(0,0)

#accl_ode = [v_ode[i]/t_ode[i] for i in range(1,len(t_ode))]
#accl_ode.insert(0,0)

print("Using inbuilt ode function at t =",t_ode[199],", x =",uf[199,0],",v =",uf[199,1]) 
print()

time = []
dist = []
vel = []



while ti <= tf:
    time.append(ti)
    dist.append(x)
    vel.append(v)
    x = x + h*funct1(x,v,ti)
    v = v + h*funct2(x,v,ti)
    ti = ti + h
    
    
print("Using euler method at t =",ti,", x =",x,",v =",v) 

#accl = [vel[i]/time[i] for i in range(1,len(time))]
#accl.insert(0,0)

accl = [funct2(dist[i],vel[i],time[i]) for i in range(1,len(time))]
accl.insert(0,0)

fig = plt.figure()
plt.subplot(2,2,1)
plt.plot(time,dist, ls = "dashed", lw = 3)
plt.plot(t_ode,x_ode)
plt.xlabel("time")
plt.ylabel("Angular Displacement")
plt.suptitle("Motion of a Simple Pendulum")
plt.tight_layout(w_pad = 6)
fig.legend(["Euler method","Inbuilt method"], loc = 'lower center')

plt.subplot(2,2,2)
plt.plot(time,vel, ls = "dashed", lw = 3)
plt.plot(t_ode,v_ode)
plt.xlabel("time")
plt.ylabel("Angular Velocity")


plt.subplot(2,2,3)
plt.plot(time,accl, ls = "dashed", lw = 3)
plt.plot(t_ode,accl_ode)
plt.xlabel("time")
plt.ylabel("Accleration")

plt.subplot(2,2,4)
plt.plot(dist,vel, ls = "dashed", lw = 3)
plt.plot(x_ode,v_ode)
plt.xlabel("Angular Displacement")
plt.ylabel("Angular Velocity")












   
    
    
    
    
    
    
