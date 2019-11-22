import matplotlib.pyplot as plt 
plt.rcParams['toolbar'] = 'None' 
import numpy as np # importando numpy

def genera_montecarlo(N=100000):
    plt.figure(figsize=(6,6))
    
    x, y = np.random.uniform(-1, 1, size=(2, N))
    interior = (x**2 + y**2) <= 1
    pi = interior.sum() * 4 / N
    error = abs((pi - np.pi) / pi) * 100
    exterior = np.invert(interior)
    plt.plot(x[interior], y[interior], 'b.')
    plt.plot(x[exterior], y[exterior], 'r.')
    plt.plot(0, 0, label='$\hat \pi$ = {:4.4f} \nerror = {:4.4f}%'.format(pi,error), alpha=0, color='g')
    plt.axis('square')
    plt.legend(frameon=True, framealpha=0.9, fontsize=16)
    plt.show()

genera_montecarlo()