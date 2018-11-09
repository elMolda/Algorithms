from Graph import *
from BruteForce import *
from Aproximation import *
from Sampler import *           


fout = open("sizes.txt",'w')
for i in range(0,101):
        G = random_graph()
        aprox = aprox_VC(G)
        brute = brute_force_VC(G)
        print("aprox ",aprox)
        print("brute ",brute)
        fout.write(str(len(brute))+","+str(len(aprox))+"\n")
fout.close()


