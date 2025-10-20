import numpy as np
from scipy.integrate import odeint

def enzyme_model(V1, Km1, V2, Km2, S0):
    def dydt(y, t, V1, Km1, V2, Km2):
        S, I, P = y
        v1 = V1 * S / (Km1 + S)
        v2 = V2 * I / (Km2 + I)
        return [-v1, v1 - v2, v2]

    y0 = [S0, 0, 0]
    t = np.linspace(0, 20, 400)
    sol = odeint(dydt, y0, t, args=(V1, Km1, V2, Km2))
    S, I, P = sol.T
    return t, S, I, P
