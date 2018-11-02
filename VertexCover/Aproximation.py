from Graph import *

def aprox_VC(G):

    C = set()
    edge_copy = G.E
    while bool(edge_copy):
        arb_edge = edge_copy.popitem()    
        C.add(arb_edge[0])
    return C
