import sys
import random
import numpy
import matplotlib.pyplot as plt

def rectangular_sample(n, a, b):
	sample_size = 0
	x_sample = []
	y_sample = []
	while sample_size <= n:
		x = random.uniform(1,a)
		y = random.uniform(1,b)
		x_sample.append(x)
		y_sample.append(y)
		sample_size = len(x_sample)

	return x_sample, y_sample

def generate_theta(a, b):
    u = random.random() / 4.0
    theta = numpy.arctan(b/a * numpy.tan(2*numpy.pi*u))

    v = random.random()
    if v < 0.25:
        return theta
    elif v < 0.5:
        return numpy.pi - theta
    elif v < 0.75:
        return numpy.pi + theta
    else:
        return -theta

def radius(a, b, theta):
   return a * b / numpy.sqrt((b*numpy.cos(theta))**2 + (a*numpy.sin(theta))**2)

def eliptical_sample(n, a, b):
	sample_size = 0
	x_sample = []
	y_sample = []
	while sample_size <= n:
		random_theta = generate_theta(a, b)
		max_radius = radius(a, b, random_theta)
		random_radius = max_radius * numpy.sqrt(random.random())
		x_sample.append(random_radius * numpy.cos(random_theta))
		y_sample.append(random_radius * numpy.sin(random_theta))
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
	x_sample , y_sample  = rectangular_sample(n,a,b)
	plt.scatter(x_sample, y_sample)
	plt.show()
elif fig == 'e':
	x_sample , y_sample  = eliptical_sample(n,a,b)
	plt.scatter(x_sample, y_sample)
	plt.show()