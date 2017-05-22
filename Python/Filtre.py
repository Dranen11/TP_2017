def Passe_bas(Temps,Data,freq_coupure):
    import numpy as np
    from scipy import fftpack

    freq_echantillonage = Temps[Temps.size-1]/Temps.size
    freqs = fftpack.fftfreq(Temps.size, d=freq_echantillonage)
    FT = fftpack.fft(Data)

    for i in range(0,Temps.size):
        if np.abs(freqs[i]) > freq_coupure :
            FT[i] = 0

    Data = np.real(fftpack.ifft(FT))
    return Data
