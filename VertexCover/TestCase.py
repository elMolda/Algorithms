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
edges['b'].append('a')
edges['b'].append('c')
edges['c'].append('b')
edges['c'].append('e')
edges['c'].append('d')
edges['d'].append('c')
edges['d'].append('e')
edges['d'].append('f')
edges['d'].append('g')
edges['e'].append('c')
edges['e'].append('d')
edges['e'].append('f')
edges['f'].append('e')
edges['f'].append('d')
edges['g'].append('d')

G = Graph(vertices, edges)

u = random.choice(list(G.E.keys()))
v = random.choice(list(G.E[u]))
print(u," ",v)




#brute_vc = brute_force_VC(G)
aprox_vc = aprox_VC(G)
#print(brute_vc)
print(aprox_vc)


