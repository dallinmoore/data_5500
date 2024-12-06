# Dallin Moore

import requests
import json
import os
import networkx as nx
import matplotlib.pyplot as plt


tickers = {"ripple":"xrp",
           "cardano":"ada",
           "bitcoin-cash":"bch",
           "eos":"eos",
           "litecoin":"ltc",
           "ethereum":"eth",
           "bitcoin":"btc",
           "link":"link"
}

base_url = 'https://api.coingecko.com/api/v3/simple/price?ids='
base_url2 = '&vs_currencies='
url = base_url+','.join([ticker for ticker in tickers])+base_url2+','.join([tickers[ticker] for ticker in tickers])

req = requests.get(url)
data = json.loads(req.text)

# create an empty graph
g = nx.DiGraph()

# add nodes to the graph
for currency in data:
    g.add_node(tickers[currency])

edges = []
# add edges to the graph
for source, targets in data.items():
    for target, weight in targets.items():
        if tickers[source] != target:
            edges.append((tickers[source], target, weight))
            # print(f"Source: {tickers[source]}, Target: {target}, Weight: {weight}")
        
g.add_weighted_edges_from(edges) 

def find_arbitrage(graph):
    arbitrage = []
    # find all simple cycles in the graph
    cycles = nx.simple_cycles(graph)

    # iterate over each cycle, going both directions
    # if there is a cycle one direction, there must be one in the other direction
    for cycle in cycles:
        opposite_cycle = cycle[::-1]
        weight_product = 1.0
        weight_product2 = 1.0
        for i in range(len(cycle) - 1):
            source = cycle[i]
            source2 = opposite_cycle[i]
            target = cycle[i + 1]
            target2 = opposite_cycle[i + 1]
            # get the weight of the edge between source and target
            weight = graph[source][target]['weight']
            weight2 = graph[source2][target2]['weight']
            weight_product *= weight
            weight_product2 *= weight2
        print(cycle, weight_product)
        print(opposite_cycle, weight_product2)

        # check if the product is greater or less than 1
        product = weight_product*weight_product2
        if product > 1 or product < 1:
            print(product)
            arbitrage.append((cycle, product))

    return arbitrage



arbitrage = find_arbitrage(g)
# find the maximum and minimum values of all the  cycles
min_value = min(arbitrage, key=lambda x: x[1])
max_value = max(arbitrage, key=lambda x: x[1])
print('-'*55)
print("Smallest paths weight factor:", min_value[1])
print("Path:",min_value[0])
print('-'*55)
print("Largest paths weight factor:", max_value[1])
print("Path:",max_value[0])


# create a visualization of the graph

# curr_dir = os.path.dirname(__file__) # get the current directory of this file
# graph_visual_fil = curr_dir + "/" + "crypto.png" 

# pos=nx.circular_layout(g) # pos = nx.nx_agraph.graphviz_layout(G)
# nx.draw_networkx(g,pos)
# labels = nx.get_edge_attributes(g,'weight')
# nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

# plt.savefig(graph_visual_fil)