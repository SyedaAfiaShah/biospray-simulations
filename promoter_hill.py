import numpy as np

def hill_expression(Emax=1.0, Kd=2.0, n=2.0):
    PAH = np.linspace(0, 10, 201)
    Expr = Emax * (PAH**n) / (Kd**n + PAH**n)
    return PAH, Expr
