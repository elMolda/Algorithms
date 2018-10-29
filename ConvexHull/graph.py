import matplotlib.pyplot as plt
import numpy as np

x, y_dac = np.loadtxt("dac_test.txt", delimiter=',', usecols=(0, 1), unpack=True)

x,y_inc = np.loadtxt("incre_test.txt", delimiter=',', usecols=(0, 1), unpack=True)

x,y_jar = np.loadtxt("jarvis_test.txt", delimiter=',', usecols=(0, 1), unpack=True)


N=6
x=[10., 100., 1000., 10000., 100000., 1000000.]
p1=plt.plot(x, y_dac)
p2=plt.plot(x, y_inc)
p3=plt.plot(x, y_jar)

#plt.bar(np.arange(N), y_inc, width)

#plt.bar(np.arange(N), y_jar, width)

plt.ylabel('Tiempo (s)')
plt.xlabel('N')
plt.title('Comparativa tiempos de ejecución')
plt.legend((p1[0], p2[0], p3[0]), ('D&C', 'Incremental', 'Jarvis'))


plt.show()
