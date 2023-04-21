from matplotlib import pyplot as plt
from scipy import signal

def main():
        sys = signal.TransferFunction([2e7], [1, 2500, 2e7])
        
        w, mag, phase = signal.bode(sys)
        
        plt.figure()
        plt.semilogx(w, mag)
        plt.grid(True)
        plt.title("Low Pass Magnitude")
        
        plt.figure()
        plt.semilogx(w, phase)
        plt.grid(True)
        plt.title("Low Pass Angle")
        
        sys = signal.TransferFunction([1, 0, 0], [1, 25000, 2e8])

        w, mag, phase = signal.bode(sys)
        
        plt.figure()
        plt.semilogx(w, mag)
        plt.grid(True)
        plt.title("High Pass Magnitude")

        plt.figure()
        plt.semilogx(w, phase)
        plt.grid(True)
        plt.title("High Pass Angle")
        
        plt.show()
        
if __name__ == "__main__":
    main()
