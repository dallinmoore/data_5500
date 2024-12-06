# Dallin Moore
# ChatGPT: How do i find the number of nodes for a graph?

import networkx as nx

def num_of_nodes(graph):
    num = 0
    for _ in graph.nodes():
        num += 1
    return num

