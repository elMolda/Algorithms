import sys
from Point import Point
import matplotlib.pyplot as plt
from sampler import rectangular_sample, eliptical_sample

n = int(sys.argv[1])
fig = str(sys.argv[2])
a = int(sys.argv[3])
b = int(sys.argv[4])
r = float(sys.argv[5])

if fig == 'r':
	sample  = rectangular_sample(n,a,b,r)
		
elif fig == 'e':
	sample  = eliptical_sample(n,a,b,r)