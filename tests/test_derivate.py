import numpy as np
import pytest

from fdce._extension._fdce import derivate as ext_derivate
from fdce.derivate import derivate as src_derivate


def _parameters():
    x = np.linspace(-5, 5, 100)
    y = x**2
    dx = x[1] - x[0]
    dxdy = (y[1:] - y[:-1]) / dx
    return [
        (x, y, 1, 1, ext_derivate, dxdy),
        (x, y, 1, 1, src_derivate, dxdy),
    ]


@pytest.mark.parametrize("x, y, order, acc, func, expected", _parameters())
def test_derivate(x, y, order, acc, func, expected):
    res = func(x, y, order, acc)
    assert res.shape == (x.shape[0] - acc,)
    assert np.allclose(res, expected)
