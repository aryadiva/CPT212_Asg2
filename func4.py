import networkx as nx
from matplotlib import pyplot as plt
import init
import random

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

def mst():
    T = nx.algorithms.minimum_spanning_tree(graph.to_undirected())
    print(T)
    nx.draw_networkx(T, with_labels=True, node_size=1500, node_color='grey', edge_color='grey', arrowsize=22,
                     font_size=16)
    ax = plt.gca()
    ax.margins(0.005)
    plt.axis("off")
    plt.show();

def random_mst():
    edges.clear()

    i = 4
    rand = random.sample(range(5), i)
    arr = []
    while i <= 4:
        arr.append(rand)
        i+=1
    edges2 = []
    i=0
    while i <= 4:
        edges2.append((vertex[arr[i]], vertex[arr[i+1]], vertex[arr[i]]+vertex[arr[i+1]]))
        i+=1
    edges.append(edges2)



