import numpy as np
import matplotlib.pyplot as plt

def logic_behavior():
    t = np.arange(0, 20, 1)
    P = np.array([1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,0])  # pollutant input
    K = np.logical_not(P).astype(int)                        # kill-switch logic
    D = np.logical_and(P, np.logical_not(K)).astype(int)     # degradation active only when P=1 and K=0
    return t, P, K, D
