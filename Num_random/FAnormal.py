
#Asignacion 1.1
#Generacion de numeros aleatorios en python
#Pertenece a: Faustino.arauz

import numpy as np

import matplotlib.pyplot as plt

mu, sigma = 0, 1 

s = np.random.normal(mu, sigma, 32000)

count, bins, ignored = plt.hist(s, 40, density=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='g')

plt.ylabel("Valores Y")
plt.xlabel("Valores X")
plt.title("Distribucion Normal")
plt.show()
