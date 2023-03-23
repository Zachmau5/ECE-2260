#!/usr/bin/python3

import scipy
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import math

def inverse_laplace(N_s, D_s, t):
    eq=scipy.signal.residue(N_s,D_s)
    f=np.zeros(np.size(t))
    constant=eq[0]
    angle=eq[1]
    print('Printing constant Value')
    print(constant[0])
    print('Printing Root Value ', end ='')
    print(angle[1])
    
    pole=angle[0]
    prepole=None
    n=1
    for i in range(len(angle)):
        pole = angle[i]
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
    #Real and Distinct
    print('Real and Distint #')
    n=np.array([0,96,1632,5760])
    d=np.array([1,14,48,0])
    t=np.arange(0,2,0.05)
    u=((120-72*(np.exp(-8*t))+48*(np.exp(-6*t))))
    f=(inverse_laplace(n,d,t))
    plt.subplot(2,2,1)
    plt.plot(t,f,linewidth=6)
    plt.plot(t,u,":",linewidth=4)
    plt.title('Real and Distinct vs Time')

    #Imaginary and distinct
    print('Imaginary and Distint #')
    n=np.complex.array([100,300])
    d=np.complex.array([1,12,61,150])
    t=np.arange(0,2,0.05)
    u=((-12*np.exp(-6*t))+np.exp(-3*t)*(12*np.cos(4*t)+16*np.sin(4*t)))
    f=(inverse_laplace(n,d,t))
    plt.subplot(2,2,2)
    plt.plot(t,f,linewidth=6)
    plt.plot(t,u,":",linewidth=4)
    plt.title('Imaginary and Distinct vs Time')

    #Real Repeated
    print('Real and Repeated #')
    t=np.arange(0,3,0.05)
    u=(20-((200*t**2))*(np.exp(-5*t))-100*t*(np.exp(-5*t))-20*(np.exp(-5*t)))
    n=np.array([100, 2500])
    d=np.array([1, 15, 75, 125, 0])
    f=inverse_laplace(n,d,t)
    plt.subplot(2,2,3)
    plt.plot(t,f,linewidth=6)
    plt.plot(t,u,":",linewidth=4)
    plt.title('Real and Repeated vs Time')

    #Imaginary Repeated
    print('Imaginary and Repeated #')
    t=np.arange(0,3,0.05)
    u=(-24*t*np.exp(-3*t)*np.cos(4*t)+6*np.exp(-3*t)*np.cos((4*t)-(np.pi/2)))
    n=np.complex.array([0,0,0,0,768])
    d=np.complex.array([1, 12, 86, 300, 625])
    f=inverse_laplace(n,d,t)
    plt.subplot(2,2,4)
    plt.plot(t,f,linewidth=6)
    plt.plot(t,u,":",linewidth=4)
    plt.title('Imaginary and Repeated vs Time')
    plt.show()

if __name__ == '__main__':
    main()
