import sys
import time
from Point import Point
import matplotlib.pyplot as plt
from sampler import rectangular_sample, eliptical_sample

def distance(a,b,c):
	y1 = a.y - b.y
	y2 = a.y -c.y
	x1 = a.x -b.x
	x2 = a.x -c.x
	x = y1 * y1 + x1 * x1
	y = y2 * y2 + x2 * x2

	if x == y:
		return 0
	elif x < y:
		return -1
	else:
		return 1

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

def jarvis_hull(points):
	start = points[0]
	for i in range(1,len(points)):
		if points[i].x < start.x:
			start = points[i]

	current = start
	result = set()
	result.add(start)
	colinear = []
	while True:
		nextTarget = points[0]
		for i in range (1,len(points)):
			if points[i] == current:
				continue

			val = crossProdcut(current,nextTarget,points[i])
			if val > 0:
				nextTarget = points[i]
				colinear = []
			elif val == 0:
				if distance(current,nextTarget,points[i]) < 0:
					colinear.append(nextTarget)
					nextTarget = points[i]
				else:
					colinear.append(points[i])

		for i in range(0,len(colinear)):
			result.add(colinear[i])

		if nextTarget == start:
			break

		result.add(nextTarget)
		current = nextTarget

	return result

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
hull = jarvis_hull(sample)
used_time = time.time() - start_time
	
x_hull = []
y_hull = []
lista = list(hull)
lista.sort(key=lambda x: x.x)#O(n log n)

i = 0
while i< len(lista)/2: 
	x_hull.append(lista[i].x)
	y_hull.append(lista[i].y)
	i = i + 1
          
j = len(lista) - 1
while j >= len(lista)/2: 
	x_hull.append(lista[j].x)
	y_hull.append(lista[j].y)
	j = j - 1

for i in range(len(lista)):
	print("("+str(x_hull[i])+","+str(y_hull[i])+")")


x = []
y = []
for i in range(len(sample)):
	x.append(sample[i].x)
	y.append(sample[i].y)

plt.scatter(x,y)
for k in range(len(x_hull)):
	plt.plot(x_hull[k:k+2],y_hull[k:k+2])
	
plt.title('Jarvis March')
plt.show()
print("--- Javis March took "+ str(used_time) +" seconds for n= "+str(n) )

