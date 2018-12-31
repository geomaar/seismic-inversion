import numpy as np
import math


def ricker(nt, dt, center_freq, t_0=None):
    """ Returns a normalized Ricker wavelet

    Args: 
        nt: Number of samples
        dt: Sampling density in sec.
        center_freq: Center frequency in Hz
        t_0: Time for center sample (peak) in sec.
        Default is center output trace: t_0 = (nt-1)/2 * dt
    Output:
        Ricker wavelet
    """

    if t_0 is None:
        t_0 = (nt-1)/2 * dt

    tmax = (nt-1)*dt
    t = np.linspace(0.0, tmax, tmax/dt)
    t = t - t_0
    arg = (np.pi * center_freq * t)**2
    return ((1-2*arg) * np.exp(-1*arg))
