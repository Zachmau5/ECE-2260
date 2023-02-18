import numpy as np
import matplotlib.pyplot as plt

def main():
    tau = 0.001
    t = np.linspace(0, 5*tau)
    f_t = 5-5*np.e**(-t/tau)
    plt.plot(t, f_t)
    plt.xlabel("Time    [s]")
    plt.ylabel(r"$V_{0}(t)$    [V]")
    plt.title(r"$V_{0}(t)$ with respect to time")
    plt.text(0.002,1,("Found value of tau: {:.2e}".format(find_time_constant(t, f_t))))
    #print (tau)
    plt.show()
    #print(find_time_constant(t, f_t))

def find_time_constant(t,f_t):
    vMax = max(f_t)
    midPoint = 0.632*vMax
    differenceArray = np.absolute(f_t - midPoint)
    index = differenceArray.argmin()
    tau = t[index]
    tau=float(tau)
    print (tau)
    return tau

if __name__ == '__main__':
    main()
