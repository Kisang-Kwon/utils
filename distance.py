import numpy as np

def euc_dist(coords1, coords2):
    return np.sqrt(np.sum(np.square(np.array(coords1) - np.array(coords2))))