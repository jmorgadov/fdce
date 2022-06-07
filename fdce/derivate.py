import numpy as np

from fdce.get_coeff import get_coeff


def derivate(
    x: np.ndarray, y: np.ndarray, order: int = 1, accuracy: int = 1
) -> np.ndarray:
    result = np.empty((x.shape[0] - accuracy,))
    a_len = accuracy + 1
    coeff_arr = np.empty((order + 1, a_len, a_len))

    for i in range(result.shape[0]):
        a = x[i : i + a_len]
        get_coeff(x[i], a, order, coeff_arr)
        result[i] = np.dot(coeff_arr[order, a_len - 1, :], y[i : i + a_len])

    return result
