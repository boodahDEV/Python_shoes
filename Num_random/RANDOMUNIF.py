
#Asignacion 1.1
#Generacion de numeros aleatorios uniformes en python

#Pertenece a: Faustino.arauz

from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

s = np.random.uniform(1,0,32000)

count, bins, ignored = plt.hist(s, 15, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')

plt.ylabel("Valores Y")
plt.xlabel("valores X")
plt.title("Distribucion Uniforme")
plt.show()
