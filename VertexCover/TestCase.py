from Graph import *
from BruteForce import *
from Aproximation import *
import random

vertices = set([])
edges = {}

vertices.add('a')
vertices.add('b')
vertices.add('c')
vertices.add('d')
vertices.add('e')
vertices.add('f')
vertices.add('g')
            

for edge in vertices:
    if not (edge in edges):
        edges[edge] = []

edges['a'].append('b')
edges['b'].append('c')
edges['c'].append('e')
edges['c'].append('d')
edges['d'].append('e')
edges['d'].append('f')
edges['d'].append('g')
edges['e'].append('f')

G = Graph(vertices, edges)

brute_vc = brute_force_VC(G)
aprox_vc = aprox_VC(G)
print(brute_vc)
print(aprox_vc)


