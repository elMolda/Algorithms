from Graph import *
from BruteForce import *
from Aproximation import *
from Sampler import *



#fout = open("sizes.txt","w+")
#for i in range(1,101):
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

'''edges[0].append(2)
edges[0].append(3)
edges[1].append(2)
edges[1].append(3)
edges[1].append(4)
edges[2].append(0)
edges[2].append(1)
edges[2].append(3)
edges[2].append(4)
edges[3].append(0)
edges[3].append(1)
edges[3].append(2)
edges[4].append(1)
edges[4].append(2)
edges['a'].append('b')
edges['b'].append('a')
edges['b'].append('c')
edges['c'].append('b')
edges['c'].append('e')
edges['e'].append('c')
edges['c'].append('d')
edges['d'].append('c')
edges['d'].append('e')
edges['e'].append('d')
edges['d'].append('f')
edges['f'].append('d')
edges['d'].append('g')
edges['g'].append('d')
edges['e'].append('f')
edges['f'].append('e')'''

fout = open("sizes2.txt",'w')
for i in range(0,101):
        G = random_graph()#Graph(vertices, edges)
        aprox = aprox_VC(G)
        brute = brute_force_VC(G)
        print("aprox ",aprox)
        print("brute ",brute)
        fout.write(str(len(brute))+","+str(len(aprox))+"\n")
fout.close()


