import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_wave_1d(x, u_all, dt_effective, mode="wave"):
    fig, ax = plt.subplots()
    line, = ax.plot(x, u_all[0])

    # Configuration selon le mode
    if mode == "wave":
        ax.set_ylim(-1, 1)
        ax.set_ylabel("Amplitude (m)")  # unité du déplacement
        titre_base = "Équation des ondes 1D"
    elif mode == "heat":
        umin = min(u.min() for u in u_all)
        umax = max(u.max() for u in u_all)
        ax.set_ylim(umin, umax)
        ax.set_ylabel("Température (K)")  # unité thermique
        titre_base = "Équation de la chaleur 1D"
    else:
        titre_base = "Simulation 1D"
        ax.set_ylabel("u")

    ax.set_xlabel("Position x (m)")
    ax.set_title(titre_base)

    def update(frame):
        line.set_ydata(u_all[frame])
        t_physique = frame * dt_effective
        ax.set_title(f"{titre_base} — Temps = {t_physique:.3f} s")
        return line,

    ani = FuncAnimation(fig, update, frames=len(u_all), interval=30)
    plt.tight_layout()
    plt.show()
