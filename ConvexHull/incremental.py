import sys
import time
from Point import Point
import matplotlib.pyplot as plt
from sampler import rectangular_sample, eliptical_sample

def incremental_hull(points):
	points.sort(key=lambda x: x.x)#O(n log n)
	upper = []
	upper.append(points[0])
	upper.append(points[1])
	for i in range(2,len(points)):
		upper.append(points[i])
		while len(upper) > 2 and crossProdcut(upper[len(upper)-3], upper[len(upper)-2], upper[len(upper)-1]) >= 0:
			del upper[len(upper)-2]

	lower = []
	lower.append(points[len(points)-1])
	lower.append(points[len(points)-2])
	for i in range(len(points) - 1, -1, -1):
		lower.append(points[i])
		while len(lower) > 2 and crossProdcut(lower[len(lower)-3], lower[len(lower)-2], lower[len(lower)-1]) >= 0:
			del lower[len(lower)-2]	

	del lower[0]
	del lower[len(lower)-1]

	hull = upper + lower

	return hull

'''
Donde está el punto c en relacion al vector ab
Retorna
	> 0 c está a la izquierda de ab
	= 0 los tres puntos son colineales
	< 0 c está a la derecha de ab
'''
def crossProdcut(a,b,c):
	y1 = a.y - b.y
	y2 = a.y - c.y
	x1 = a.x - b.x
	x2 = a.x - c.x
	return y2 * x1 - y1 * x2

n = int(sys.argv[1])
fig = str(sys.argv[2])
a = int(sys.argv[3])
b = int(sys.argv[4])
r = float(sys.argv[5])

if fig == 'r':
	sample  = rectangular_sample(n,a,b,r)
		
elif fig == 'e':
	sample  = eliptical_sample(n,a,b,r)

start_time = time.time()
hull = incremental_hull(sample)
used_time = time.time() - start_time


x_hull = []
y_hull = []

for p in hull:
	print(str(p))
	x_hull.append(p.x)
	y_hull.append(p.y)

x = []
y = []
for i in range(len(sample)):
	x.append(sample[i].x)
	y.append(sample[i].y)

plt.scatter(x,y)
plt.scatter(x_hull,y_hull,facecolor='red')
plt.show()
print("--- Incremental took "+ str(used_time) +" seconds for n= "+str(n) )