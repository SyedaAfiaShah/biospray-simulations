import numpy as np

def system_dynamics(decay_rate=0.3, kill_threshold=0.1):
    t = np.linspace(0, 10, 200)
    PAH = np.exp(-decay_rate * t)
    Enzyme = 1 - np.exp(-decay_rate * t)
    Kill = (PAH < kill_threshold).astype(float)
    return t, PAH, Enzyme, Kill
