import random
import numpy as np
from Point import Point

def rectangular_sample(n, a, b, r):
	sample_size = 0
	sample = []

	while sample_size < n:
		x = random.uniform(1,a)
		y = random.uniform(1,b)
		x_rot = (x * np.cos(r)) - (y * np.sin(r))
		y_rot = (x * np.sin(r)) + (y * np.cos(r))
		point = Point(x_rot,y_rot)
		sample.append(point)
		sample_size = len(sample)

	return sample

def generate_theta(a, b):
    u = random.random() / 4.0
    theta = np.arctan(b/a * np.tan(2*np.pi*u))

    v = random.random()
    if v < 0.25:
        return theta
    elif v < 0.5:
        return np.pi - theta
    elif v < 0.75:
        return np.pi + theta
    else:
        return -theta

def radius(a, b, theta):
   return a * b / np.sqrt((b*np.cos(theta))**2 + (a*np.sin(theta))**2)

def eliptical_sample(n, a, b, r):
	sample_size = 0
	sample = []

	while sample_size < n:
		random_theta = generate_theta(a, b)
		max_radius = radius(a, b, random_theta)
		random_radius = max_radius * np.sqrt(random.random())
		x = random_radius * np.cos(random_theta)
		y = random_radius * np.sin(random_theta)
		x_rot = (x * np.cos(r)) - (y * np.sin(r))
		y_rot = (x * np.sin(r)) + (y * np.cos(r))		
		point = Point(x_rot,y_rot)
		sample.append(point)
		sample_size = len(sample)

	return sample
		