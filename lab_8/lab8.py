# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:32:01 2023

@author: halle
"""

import scipy
import matplotlib.pyplot as plt
import numpy as np
import math

def inverse_laplace(N_s, D_s, t):
    eq=scipy.signal.residue(N_s,D_s)
    f=np.zeros(np.size(t))
    constant=eq[0]
    angle=eq[1]
    print('Printing constant Value ', end ='')
    print(constant)
    print('Printing Angle Value ', end ='')
    print(angle)
    
    pole=angle[0]
    prepole=None
    n=1
    for i in range(len(angle)):
        pole=angle[i]
        if pole == prepole:
            n+=1
        else:
            n=1
        prepole=angle[i]
        f=f+(constant[i]*t**(n-1)*np.exp(angle[i]*t))/math.factorial(n-1)
    return f
def graph(t,f):
    plt.plot(t,f)
    plt.xlabel('Time (s)')
    plt.ylabel('f(t)')

def main():
    t=np.arange(0,3,0.5)
    #Real and Distinct
    print('Real and Distint #')
    n=np.array([120,48,-72])
    d=np.array([0,-6,-8])
    t=np.arange(0,3,0.05)
    f=inverse_laplace(n,d,t)
    graph(t,f)
    plt.title('Real and Distinct vs Time')
    plt.show()
    
if __name__ == '__main__':
    main()
