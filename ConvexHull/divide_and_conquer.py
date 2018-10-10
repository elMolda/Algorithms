import sys
import time
import math
from Point import Point
import matplotlib.pyplot as plt
from sampler import rectangular_sample, eliptical_sample

def dac_hull(points):

	min_p, max_p = max_min_x(points)

	hull = dac_hull_aux(points, min_p, max_p)

	hull = hull + dac_hull_aux(points, max_p, min_p)

	return hull



def dac_hull_aux(points, min_p, max_p):
	left_points = get_points_left(min_p, max_p, points)

	ptC = point_max_from_line(min_p, max_p, left_points)

	if ptC == None:
		return [max_p]

	hull = dac_hull_aux(left_points, min_p, ptC)

	hull = hull + dac_hull_aux(left_points, ptC, max_p)

	return hull


def get_points_left(start, end, points):
	left_points = []
	for pt in points:
		if crossProdcut(start,end,pt) > 0:
			left_points.append(pt)

	return left_points

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

def point_max_from_line(start, end, points):
	max_dist = -math.inf

	for point in points:
		if point != start and point != end:
			dist = distance(start, end, point)
			if dist > max_dist:
				max_dist = dist
				max_point = point

	if max_dist != -math.inf:
		return max_point
	else:
		return None

def max_min_x(points):
	min_x = math.inf
	max_x = -math.inf

	for i in range(len(points)):
		if points[i].x > max_x:
			max_x = points[i].x
			max_index = i
		if points[i].x < min_x:
			min_x = points[i].x
			min_index = i

	return Point(points[min_index].x,points[min_index].y), Point(points[max_index].x,points[max_index].y)

def distance(start, end, point): 
	nom = abs((end.y - start.y) * point.x - (end.x - start.x) * point.y + end.x * start.y - end.y * start.x)
	denom = ((end.y - start.y)**2 + (end.x - start.x) ** 2) ** 0.5
	result = nom / denom
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
hull = dac_hull(sample)
print("--- Divide & Conquer took "+ str(time.time() - start_time) +" seconds for n= "+str(n) )


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