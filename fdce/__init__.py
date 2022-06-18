"""
Python implementation of the algorithm presented in:

> Fornberg, B. (1988). Generation of finite difference formulas on arbitrarily
  spaced grids. Mathematics of computation, 51(184), 699-706.

This algorithm can estimate the coefficients of the finite difference formula
used to estimate any derivative of an unidimensional function at a point `x_0`
given a grid of points (mostly neighbors of `x_0`). The accuracy level is
determined by the number of grid points used in each estimation.
"""

try:
    from fdce._extension._fdce import derivative, get_coeff
except ImportError:
    from fdce.differentiation import derivative
    from fdce.get_coeff import get_coeff

__version__ = "0.1.2a1"
__all__ = ["get_coeff", "derivative"]
