import random
import math
from Point import Point

def rectangular_sample(n, a, b, r):
	sample_size = 0
	sample = []

	while sample_size < n:
		x = random.uniform(1,a)
		y = random.uniform(1,b)
		x_rot = (x * math.cos(r)) - (y * math.sin(r))
		y_rot = (x * math.sin(r)) + (y * math.cos(r))
		point = Point(x_rot,y_rot)
		sample.append(point)
		sample_size = len(sample)

	return sample

def generate_theta(a, b):
    u = random.random() / 4.0
    theta = math.atan(b/a * math.tan(2*math.pi*u))

    v = random.random()
    if v < 0.25:
        return theta
    elif v < 0.5:
        return math.pi - theta
    elif v < 0.75:
        return math.pi + theta
    else:
        return -theta

def radius(a, b, theta):
   return a * b / math.sqrt((b*math.cos(theta))**2 + (a*math.sin(theta))**2)

def eliptical_sample(n, a, b, r):
	sample_size = 0
	sample = []

	while sample_size < n:
		random_theta = generate_theta(a, b)
		max_radius = radius(a, b, random_theta)
		random_radius = max_radius * math.sqrt(random.random())
		x = random_radius * math.cos(random_theta)
		y = random_radius * math.sin(random_theta)
		x_rot = (x * math.cos(r)) - (y * math.sin(r))
		y_rot = (x * math.sin(r)) + (y * math.cos(r))		
		point = Point(x_rot,y_rot)
		sample.append(point)
		sample_size = len(sample)

	return sample
		