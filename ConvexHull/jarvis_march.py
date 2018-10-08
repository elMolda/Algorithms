import sys
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

def crossProdcut(a,b,c):
	y1 = a.y - b.y
	y2 = a.y - c.y
	x1 = a.x - b.x
	x2 = a.x -c.x
	return y2 * x1 - y1 * x2

def jarvis_hull(points):
	start = points[0]
	for i in range(1,len(points)):
		if points[i].x < start.x:
			start = points[i]

	current = start
	result = set()
	colinear = []
	while(True):
		nextTarget = points[0]
		for i in range(1,len(points)):
			if points[i] == current:
				continue

			val = crossProdcut(current,nextTarget,points[i])
			#val > 0 points[i] esta a la izquierda de current->next
			#se cambia el nextTarget, se limpia los colineales
			if val > 0:
				nextTarget = points[i]
				colinear.clear()
			#val == 0 current next y points[i] colineales, escoger el mas lejano de cur
			elif val == 0:
				if distance(current,nextTarget,points[i]) < 0:
					colinear.append(nextTarget)
					nextTarget = points[i]
				else:
					colinear.append(points[i])
		for j in range(len(colinear)):
			result.add(colinear[j])

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
	hull = jarvis_hull(sample)
	x_hull = []
	y_hull = []
	for p in hull:
		x_hull.append(p.x)
		y_hull.append(p.y)

	x = []
	y = []
	for i in range(len(sample)):
		x.append(sample[i].x)
		y.append(sample[i].y)
	
	plt.scatter(x,y)
	print(len(x_hull))
	print(len(y_hull))

	plt.show()
elif fig == 'e':
	sample  = eliptical_sample(n,a,b,r)
	hull = jarvis_hull(sample)
	for p in hull:
		print(str(p))
	'''x = []
	y = []
	for i in range(len(sample)):
		x.append(sample[i].x)
		y.append(sample[i].y)
	plt.scatter(x,y)
	plt.show()'''