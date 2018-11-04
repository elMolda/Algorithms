from Graph import *

def aprox_VC(G):

    C = set()
    edge_copy = G.E
    while bool(edge_copy):
        arb_edge = edge_copy.popitem()
        C.add(arb_edge[0])
        remove_incident(arb_edge,edge_copy)
    return C

def remove_incident(edge,edges):
    
    for val in edge[1]:
        if val in edge[1] and val in edges:
            del edges[val]
    if edge[0] in edges:
        del edges[edge[0]]

