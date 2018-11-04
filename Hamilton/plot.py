import matplotlib.pyplot as plt
import numpy as np

#bf = np.loadtxt("bf_costs.txt", usecols=(0), unpack=True)
bf = np.loadtxt("bf_times.txt", usecols=(0), unpack=True)

#pri = np.loadtxt("prim_costs.txt", usecols=(0), unpack=True)
pri = np.loadtxt("prim_times.txt", usecols=(0), unpack=True)

x = [i for i in range(1,101)]

print(len(bf))
print(len(pri))
print(len(x))

p2=plt.plot(x, bf)
p1=plt.plot(x, pri)

plt.ylabel('Tiempo (ms)')
plt.xlabel('Indice Grafo')
plt.title('Comparativa Tiempos de Ejecucion para PAV')
plt.legend((p1[0], p2[0]), ('Prim', 'Fuerza Bruta'))

plt.show()