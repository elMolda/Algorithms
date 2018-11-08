from Graph import *

def aprox_VC(G):

    C = set()
    edge_copy = G.E.copy()
    while bool(edge_copy):
        arb_edge = edge_copy.popitem()
        if len(arb_edge[1]) == 0:
            continue
        C.add(arb_edge[0])
        for val in arb_edge[1]:
            if arb_edge[0] in edge_copy[val]:
                edge_copy[val].remove(arb_edge[0])
    
    return C


def check_vertex_cover(G, S):
        
    for start in G.E.keys():
        if start in S:
            continue
        for end in G.E[start]:
            if not (end in S):
                return False
    return True