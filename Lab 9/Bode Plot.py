from matplotlib import pyplot as plt
from scipy import signal

def main():
        sys = signal.TransferFunction([2e7], [1, 2500, 2e7])
        w, mag, phase = signal.bode(sys)
        fig=plt.figure(figsize=(20,15))
        fig.suptitle("High and Low Pass Bode Plots",fontsize=40)
        plt.subplot(2,2,1)
        plt.semilogx(w, mag)
        plt.grid(True)
        plt.title("Low Pass Magnitude")
        plt.subplot(2,2,2)
        plt.semilogx(w, phase)
        plt.grid(True)
        plt.title("Low Pass Angle")
        
        sys = signal.TransferFunction([1, 0, 0], [1, 25000, 2e8])

        w, mag, phase = signal.bode(sys)
        
        plt.subplot(2,2,3)
        plt.semilogx(w, mag)
        plt.grid(True)
        plt.title("High Pass Magnitude")

        plt.subplot(2,2,4)
        plt.semilogx(w, phase)
        plt.grid(True)
        plt.title("High Pass Angle")      
        plt.savefig("Bode Plot.png")
        plt.show()
        
        
if __name__ == "__main__":
    main()
