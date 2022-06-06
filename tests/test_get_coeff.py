import numpy as np

from fdce._extension._fdce import get_coeff as ext_get_coeff
from fdce.get_coeff import get_coeff


def test_ext_vs_py():
    a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    x_0 = 0
    res1 = np.zeros((5, 9, 9))
    res2 = np.zeros((5, 9, 9))
    res1 = ext_get_coeff(x_0, a, 4, res1)
    res2 = get_coeff(x_0, a, 4, res2)
    assert np.allclose(res1, res2)
