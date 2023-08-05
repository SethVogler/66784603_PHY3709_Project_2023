from constants import x_min, x_max, N, dx
from numerov_algorithm import numerov
import numpy as np

def find_energy():
    """Bisection method to find energy eigenvalues"""
    E_lower, E_upper = 0.1, 2.0
    tolerance = 1e-5
    max_iter = 100

    for _ in range(max_iter):
        E_mid = (E_lower + E_upper) / 2
        psi = numerov(0.0, 0.1, E_mid)
        if np.sign(psi[-1]) != np.sign(numerov(0.0, 0.1, E_lower)[-1]):
            E_upper = E_mid
        else:
            E_lower = E_mid

        if abs(E_upper - E_lower) < tolerance:
            return E_mid

    raise Exception("Energy eigenvalue not found within tolerance.")
