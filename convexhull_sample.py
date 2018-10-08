import sys
import random
import numpy as np
import matplotlib.pyplot as plt

def rectangular_sample(n, a, b, r):
	sample_size = 0
	x_sample = []
	y_sample = []
	while sample_size <= n:
		x = random.uniform(1,a)
		y = random.uniform(1,b)
		x_rot = (x * np.cos(r)) - (y * np.sin(r))
		y_rot = (x * np.sin(r)) + (y * np.cos(r))
		x_sample.append(x_rot)
		y_sample.append(y_rot)
		sample_size = len(x_sample)

	return x_sample, y_sample

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
	x_sample = []
	y_sample = []

	while sample_size <= n:
		random_theta = generate_theta(a, b)
		max_radius = radius(a, b, random_theta)
		random_radius = max_radius * np.sqrt(random.random())
		x = random_radius * np.cos(random_theta)
		y = random_radius * np.sin(random_theta)
		x_rot = (x * np.cos(r)) - (y * np.sin(r))
		y_rot = (x * np.sin(r)) + (y * np.cos(r))		
		x_sample.append(x_rot)
		y_sample.append(y_rot)
		sample_size = len(x_sample)

	return x_sample, y_sample
		
n = int(sys.argv[1])
fig = str(sys.argv[2])
a = int(sys.argv[3])
b = int(sys.argv[4])
r = float(sys.argv[5])


print('N: '+str(n))
print('Figura: '+str(fig))
print('a: '+str(a))
print('b '+str(b))
print('r: '+str(r))


if fig == 'r':
	x_sample , y_sample  = rectangular_sample(n,a,b,r)
	plt.scatter(x_sample, y_sample)
	plt.show()
elif fig == 'e':
	x_sample , y_sample  = eliptical_sample(n,a,b,r)
	plt.scatter(x_sample, y_sample)
	plt.show()