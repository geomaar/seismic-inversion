import numpy as np

def next_power_of_2(x):
    return 1 if x == 0 else 2**math.ceil(math.log2(x))

def butterworth(Fmin=10, Fmax=75, dt=0.002, Nt=101, Order=10):
    """ Returns butterworth bandpass filter coefficients
    
    Args:
        Fmin: Bandpass low frequency (Hz). Optional. Default = 10
        Fmax: Bandpass high frequency (Hz). Optional. Default = 70
        dt: Sample interval of Seismic and Impedance (sec). Optional.Default = 0.002
        Nt: Number of samples. Optional. Default=101
        Order: Butterworth order. Optional. Default=10

    Returns:
        wavelet: Butterworth bandpass filter coefficients
        spec: Amplitude spectrum
        f: Frequencies corresponding to spec
    """

    
    NFFT = 2**next_power_of_2(Nt) # Next power of 2
    m = NFFT/2+1
    fnq = 1/(2*dt) # Nyquist frequency 
    f = np.linspace(0,fnq,m)

    # Butterworth digital BP filter:
    passband = [Fmin/fnq Fmax/fnq] # Normalized low and high frequencies
    [Bp,Ap] = butter(Order,passband) # Butterworth digital BP filter design
    spec = [abs(freqz(Bp,Ap,m))] # Frequency response of digital filter

    Y = spec
    for k=1:NFFT/2-1:
        Y(m+k) = conj(Y(m-k)) # Complex conj negative freq


    # Filter coeff.:
    y = np.fft.ifft(Y)
    w = fftshift(y)
    wavelet = w(NFFT-Nt+1:NFFT)