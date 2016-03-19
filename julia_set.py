import numpy as np
import pylab as plt
import matplotlib
import time
from itertools import product

def julia_iteration(z, c, maxiter=256):
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return n

def julia_set(w, h, c, maxiter=256):
    start = time.perf_counter()
    m = np.empty((h, w), dtype=np.uint8)
    for x, y in product(range(w), range(h)):
        z = (x-w/2)/(h/2) + (y-h/2)/(h/2)*1j
        m[y,x] = julia_iteration(z, c, maxiter)

    print(time.perf_counter()-start)
    return m

def plot_julia(w, h, cre, cim, cmap):
    m = julia_set(w, h, cre+cim*1j)
    cm = getattr(matplotlib.cm, cmap)
    plt.imshow(m, cmap=cm)
    plt.gca().axis('off')
    plt.show()


if __name__ == '__main__':
    # -0.8 + 0.156*1j
    #  0.3 + 0.230*1j
    plot_julia(800, 600, -0.8, 0.156, 'viridis')

    