import numpy as np

def gassmann(K_0, K_dry, K_fl, por):
    """Calculation of Gassmann equation.
    
    Args:
        K_0: Mineral bulk modulus (scalar)
        K_dry: Dry rock frame (skeleton) bulk modulus (vector)
        K_fl: Fluid bulk modulus (scalar)
        por: Porosity (vector)

    Returns: 
        K_sat: Saturated rock bulk modulus.
    """
    a = (1- np.divide(K_dry, K_0))**2
    b = np.divide(por,K_fl) + np.divide(1-por,K_0) - np.divide(K_dry,K_0**2)

    return K_dry + np.divide(a, b, where=(b != 0))

def gassmanninv(K_0,K_sat,K_fl,por):
    """ Calculation of inverse Gassmann equation.
    
    Args:
        K_0: Mineral bulk modulus (scalar)
        K_sat: Saturated rock bulk modulus (vector)
        K_fl: Fluid bulk modulus (scalar)
        por: Porosity (vector)
    
    Returns:
        K_dry: Dry rock frame (skeleton) bulk modulus (vector)
    """

    a = ( por*K_0)/ K_fl  + 1 - por
    b = ( por*K_0)/ K_fl  + K_sat/K_0 - 1 - por
    K_dry = np.divide(K_sat*a-K_0,b )
    return K_dry
