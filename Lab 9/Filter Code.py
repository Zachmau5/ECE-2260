import numpy as np
import sounddevice as sd
import soundfile as sf

def main():
    t=np.arange(0,6,1e-4)
    h_lp=(2*(1164.5)*np.exp(-1250*t)*np.cos(500*np.sqrt(295))*t-np.deg2rad(90))
    h_hp=(2*(12520.07)*np.exp(-1250*t)*np.cos(5000*np.sqrt(7))*t-np.deg2rad(176.7))
    filename = "handel.wav"
    data, fs = sf.read(filename, dtype='float32')
    data = data[:,0]
    data_lp = np.convolve(data, h_lp)
    data_lp /= max(abs(data_lp))
    data_hp = np.convolve(data, h_hp)
    data_hp /= max(abs(data_hp))
    
    sound_break = np.zeros(fs*2)
    
    data_play = np.hstack((sound_break, data,
                           sound_break, data_lp,
                           sound_break, data,
                           sound_break, data_hp))
    sd.play(data_play, fs)
    
if __name__ == "__main__":
    main()
   
