import numpy as np

from fdce._extension._fdce import get_coeff as ext_get_coeff
from fdce.get_coeff import get_coeff as src_get_coeff


def test_ext_vs_py():
    a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    res1 = ext_get_coeff(0, a, 4)
    res2 = src_get_coeff(0, a, 4)
    assert np.allclose(res1, res2)
