from gassmann import gassmann

import numpy as np


def test_all_scalars():
    g = gassmann(2, 1, 1, 1)
    assert g == 1.3333333333333333

#def test_k0_vector():
#    g = gassmann(np.array([1, 2, 3]), 1, 1, 1)
#    assert np.all(g == np.array([4, 5, 6]))