# Dallin Moore
# Chat GPT: How do I see what nodes my node is connected to? (Answer: .neighbors())

import networkx as nx

def num_nodes_degree_higher(graph,degree_higher):
    num = 0 
    
    for node in graph.nodes():
        degree = 0
        for _ in graph.neighbors(node):
            degree += 1
        if degree > degree_higher:
            num += 1
    
    return num
    