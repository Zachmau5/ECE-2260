

#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('Lab 7.xlsx',sheet_name='Sheet1')
df=np.array(df)

#Calculates Impedences from a series circuit
def Zs(R,L,C,f):
    z=R+(-1j/(C*f*2*np.pi))+(L*1j*f*2*np.pi)
    return z
#Calculates Impedences from a parallel circuit
def Zp(R,L,C,f):
    z=1/(1/R+((C*2*np.pi*f)/(-1j))+(1/(1j*2*np.pi*f*L)))
    return z
#Calculates the max/min from the array
def find_omega_o(Z,omega, circuit_type):
    if circuit_type=="parallel":
        print("Parallel")
        mx=np.argmax(np.absolute(Z))
        omega_o=omega[mx]
        f_o=omega_o/(2*np.pi)
        omega_o = "{:.2f}".format(omega_o)
        omega_o=("\u03C9\u2080 is: "+str(omega_o)+" rad/sec")
        f_o="f\u2080 {:.2f} Hz".format(f_o)
        return omega_o,f_o
    elif circuit_type=="series":
        print("Series")
        mn=np.argmin(np.absolute(Z))
        omega_o=omega[mn]
        f_o=omega_o/(2*np.pi)
        omega_o = "{:.2f}".format(omega_o)
        omega_o=("\u03C9\u2080 is: "+str(omega_o)+" rad/sec")
        f_o="f\u2080 {:.2f} Hz".format(f_o)
        return omega_o,f_o
    else:
        print("Format must be, Array, Array, String")

def main():
    f=np.logspace(3,5,num=2000)
    g=np.logspace(3,5, num=20)
    parallel=Zp(100,4.7e-3,0.033e-6,f)
    series=Zs(1000,4.7e-3,0.033e-6,f)
    Mag=np.absolute(Zs(1000,4.7e-3,0.033e-6,f))
    Mag_1=np.absolute(Zs(1000,4.7e-3,0.033e-6,g))
    
    
    
    Ang=np.angle(Zs(1000,4.7e-3,0.033e-6,f), deg=True)
    Ang_1=np.angle(Zs(1000,4.7e-3,0.033e-6,g), deg=True)
    Magp=np.absolute(Zp(1000,4.7e-3,0.033e-6,f))
    Angp=np.angle(Zp(1000,4.7e-3,0.033e-6,f),deg=True)
    
    
    y=df[:,1]
    x=df[:,0]
    fig, axs = plt.subplots(2)
    fig.set_figheight(9)
    fig.set_figwidth(9)
    axs[0].set_ylabel("Magnitude [\u2126]")
    axs[0].set_title("Series Circuit Magnitude and Phase Angle")
    axs[1].set_ylabel("Phase [\u00B0]")
    #axs[0].set_xlabel("Frequency (Hz)")
    axs[1].set_xlabel("Frequency [Hz]")
    axs[0].set_xscale('log')
    axs[0].set_yticks([2000,3000,4000])
    # axs[0].set_title("Magnitude")
    axs[0].plot(f,Mag)
    #axs[0].plot(g,y,":",c='red')
    axs[1].set_yticks([-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100])
    axs[1].set_xscale('log')
    #axs[1].set_title("Angle")
    axs[1].plot(f,Ang)
    plt.savefig('Series_Circuit.png')
    plt.show()
    
    # Second Graph plot
    
    fig, axs = plt.subplots(2)
    fig.set_figheight(9)
    fig.set_figwidth(9)
    axs[0].set_ylabel("Magnitude [\u2126]")
    axs[0].set_title("Parallel Circuit Magnitude and Phase Angle")
    axs[1].set_ylabel("Phase [\u00B0]")
    axs[1].set_xlabel("Frequency [Hz]")
    axs[0].set_xscale('log')
    axs[0].set_yticks([250,500,750,1000])
    axs[0].plot(f,Magp)
    axs[1].set_yticks([-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100])
    axs[1].set_xscale('log')
    axs[1].plot(f,Angp)
    plt.savefig('Parallel_Circuit.png')
    plt.show()
    
    fig, ax=plt.subplots(2)
    fig.set_figheight(9)
    fig.set_figwidth(9)
    x=df[:,0]
    y=df[:,1]
    y2=Mag_1
    y3=Ang_1
    ax[0].set_xscale('log')
    ax[0].set_yticks([2000,4000])
    ax[0].set_ylabel("Magnitude [\u2126]")
    ax[0].set_xlabel('Frequency [Hz]')
    ax[0].plot(x,y,label='Measured')
    ax[0].plot(x,y2, label='Coded')
    ax[0].set_title("Coded Vs Measured Values")
    y3=Ang_1
    h=df[:,2]
    ax[1].set_xscale('log')
    ax[1].set_yticks([-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100])
    ax[1].set_ylabel("Magnitude [\u2126]")
    ax[1].set_xlabel('Frequency [Hz]')
    ax[1].plot(g,h,label='Measured')
    ax[1].plot(g,y3,label='Coded')
    plt.legend()
    plt.savefig('Comparison.png')
    plt.show()
   
   
    def calc(i):
        if i=="parallel":
            Z=parallel
            print(find_omega_o(Z, (f*2*np.pi), "{}".format(i)))
        elif i=="series":
            Z=series
            print(find_omega_o(Z, (f*2*np.pi), "{}".format(i)))
        else:
            print("'seres' and 'parallel' are the only valid inputs, they are case sensitive")
    calc('parallel')
    calc('series')

if __name__ == '__main__':
    main()
