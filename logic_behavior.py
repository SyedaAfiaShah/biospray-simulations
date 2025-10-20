import numpy as np
import matplotlib.pyplot as plt

def logic_behavior():
    t = np.arange(0, 20, 1)
    P = np.array([1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,0])
    K = np.roll(np.logical_not(P).astype(int), 1) 
    K[0] = 0
    D = np.logical_and(P, np.logical_not(K)).astype(int)
    return t, P, K, D

