
from constants import x_min, x_max, N, dx
def numerov(psi0, psi1, E):
    """Numerov algorithm for solving the Schrödinger equation"""

    # Exception handling for invalid input
    if not isinstance(psi0, (int, float)) or not isinstance(psi1, (int, float)):
        raise ValueError("Initial wave function values must be numeric.")
    if not isinstance(E, (int, float)):
        raise ValueError("Energy must be numeric.")

    psi = np.zeros(N)
    psi[0], psi[1] = psi0, psi1

    # Calculate f(x) = 2 * (V(x) - E)
    f = 2 * (V(np.linspace(x_min, x_max, N)) - E)

    # Numerov iteration
    for n in range(1, N - 1):
        numer = 2 * (1 - 5/12 * dx**2 * f[n]) * psi[n] - (1 + 1/12 * dx**2 * f[n-1]) * psi[n-1]
        denom = 1 + 1/12 * dx**2 * f[n+1]
        psi[n+1] = numer / denom

    return psi
