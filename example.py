"""
This example shows how to use the coeffitients once estimated.

This interpolates and estimates the first and second derivatives of the function
f(x) = x^3 using the implemented method.

    - First derivative: f'(x) = 3x^2
    - Second derivative: f''(x) = 6x
"""

import matplotlib.pyplot as plt
import numpy as np

from fornberg import get_coeff

x = np.arange(-3, 3, 0.01)
y = x**3

new_x = x[2:-2]
dx = np.empty_like(new_x)
ddx = np.empty_like(new_x)

coeff_matrix = None
for i in range(dx.shape[0]):
    j = i + 2
    a = x[j - 2 : j + 3]
    N = a.shape[0]
    x_0 = x[j]

    # Estimate the coefficients till the second derivative
    coeff_matrix = get_coeff(x_0, a, 2, coeff_matrix)

    # First derivative
    coeff = coeff_matrix[1, N - 1, :]
    dx[i] = np.sum(coeff * y[j - 2 : j + 3])

    # Second derivative
    coeff = coeff_matrix[2, N - 1, :]
    ddx[i] = np.sum(coeff * y[j - 2 : j + 3])

plt.plot(new_x, dx, label="First derivative: $f'(x) = 3x^2$")
plt.plot(new_x, ddx, label="Second derivative: $f''(x) = 6x$")
plt.grid()
plt.legend()
plt.show()
