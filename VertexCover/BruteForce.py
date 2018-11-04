import itertools
from Graph import *

def brute_force_VC(G):
    
    for k in range(1, len(G.V) + 1):
        for subset in itertools.combinations(G.V, k):
            if check_vertex_cover(G, set(subset)):
                return (set(subset))
    return (None)

def check_vertex_cover(G, S):
        
    for start in G.E.keys():
        if start in S:
            continue
        for end in G.E[start]:
            if not (end in S):
                return False
    return True