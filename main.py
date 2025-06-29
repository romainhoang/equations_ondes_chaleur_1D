from solver import solve_wave_1d, solve_heat_1d
from animate import animate_wave_1d

def main():
    print("Quel modèle souhaitez-vous simuler ?")
    print("1 : Équation des ondes 1D")
    print("2 : Équation de la chaleur 1D")
    choix = input("Entrez 1 ou 2 : ").strip()

    # Paramètres physiques (unités SI)
    L = 1.0       # m (longueur)
    T = 1.0       # s (durée simulée)
    nx = 200      # nombre de points spatiaux

    if choix == "1":
        c = 1.0   # m/s (vitesse de l'onde)
        dt = 0.0005  # s
        x, u_all, dt_eff = solve_wave_1d(L=L, T=T, c=c, nx=nx, dt=dt)
        mode = "wave"
    elif choix == "2":
        D = 1.0   # m²/s (diffusivité thermique) prendre D = 0.1 pour observer une évolution plus lente
        dt = 0.00001  # s
        x, u_all, dt_eff = solve_heat_1d(L=L, T=T, D=D, nx=nx, dt=dt)
        mode = "heat"
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        return

    animate_wave_1d(x, u_all, dt_eff, mode=mode)

if __name__ == "__main__":
    main()
