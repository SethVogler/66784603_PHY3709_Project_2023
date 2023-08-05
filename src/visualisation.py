from numerov_algorithm import numerov
from constants import x_min, x_max, N, dx
from potential import V
import matplotlib.pyplot as plt
import numpy as np
def plot_results(E):
    """Plot the wave function and potential"""
    psi = numerov(0.0, 0.1, E)
    x = np.linspace(x_min, x_max, N)

    plt.plot(x, psi, label='Wave function')
    plt.plot(x, V(x), label='Potential')
    plt.legend()
    plt.xlabel('Position')
    plt.ylabel('Value')
    plt.title(f'Schrödinger Equation Simulation, E = {E}')
    plt.show()
