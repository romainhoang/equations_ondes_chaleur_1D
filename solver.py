import numpy as np

def solve_wave_1d(L, T, c, nx, dt):
    """
    Simule l'équation des ondes 1D : ∂²u/∂t² = c² ∂²u/∂x²
    u : déplacement (m)
    x : position (m)
    t : temps (s)
    c : vitesse de l'onde (m/s)
    """
    dx = L / (nx - 1)                 # m (espacement spatial)
    x = np.linspace(0, L, nx)         # m
    nt = int(T / dt)                  # nombre d'itérations
    r = (c * dt / dx)**2              # sans unité (stabilité numérique)

    if r > 1:
        raise ValueError(f"Instabilité numérique (onde) : r = {r:.2f} > 1")

    u_curr = np.exp(-100 * (x - L/2)**2)  # m, déplacement initial (bosse)
    u_prev = u_curr.copy()               # m, vitesse initiale nulle
    u_all = [u_curr.copy()]

    for n in range(nt):
        u_next = np.zeros_like(u_curr)
        u_next[1:-1] = (
            2 * u_curr[1:-1] - u_prev[1:-1] +
            r * (u_curr[2:] - 2 * u_curr[1:-1] + u_curr[:-2])
        )
        u_prev, u_curr = u_curr, u_next

        if n % 10 == 0:
            u_all.append(u_curr.copy())

    return x, u_all, dt * 10  # x en m, u en m, dt_effectif en s


def solve_heat_1d(L, T, D, nx, dt):
    """
    Simule l'équation de la chaleur 1D : ∂u/∂t = D ∂²u/∂x²
    u : température (K)
    x : position (m)
    t : temps (s)
    D : diffusivité thermique (m²/s)
    """
    dx = L / (nx - 1)                 # m
    x = np.linspace(0, L, nx)         # m
    nt = int(T / dt)                  # nombre d'itérations
    r = D * dt / dx**2                # sans unité (stabilité)

    if r > 0.5:
        raise ValueError(f"Instabilité numérique (chaleur) : r = {r:.2f} > 0.5")

    u = np.exp(-100 * (x - L/2)**2)   # K, température initiale
    u_all = [u.copy()]

    frame_interval = int(0.005 / dt)  # pour dt_effectif constant (≈ onde)

    for n in range(nt):
        u_new = u.copy()
        u_new[1:-1] = u[1:-1] + r * (u[2:] - 2*u[1:-1] + u[:-2])
        u = u_new

        if n % frame_interval == 0:
            u_all.append(u.copy())

    return x, u_all, 0.005  # x en m, u en K, dt_effectif en s
