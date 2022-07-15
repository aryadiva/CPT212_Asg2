import networkx as nx
from matplotlib import pyplot as plt
from common_func import add
import init
import random
from func1 import is_strongly_connected

# initialize variables from other files
graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

# function for displaying minimum spanning tree
def mst():
    T = nx.algorithms.minimum_spanning_tree(graph.to_undirected())
    print(T)
    nx.draw_networkx(T, with_labels=True, node_size=1200, node_color='grey', edge_color='grey', arrowsize=22,
                     font_size=16)
    ax = plt.gca()
    ax.margins(0.005)
    plt.axis("off")
    plt.show();

# function for randomizing algorithm
def randomize(a, b):
    i = 0
    while i < 5:
        if(a[i] == b[i]):
            while True:
                temp = random.sample(a, 5)
                b = temp
                if(a[i] != b[i]):
                    break;
        add(a[i], b[i])
        i+=1

# final function for randomizing edges
def random_mst():
    edges.clear()
    graph.clear()
    edg1 = random.sample(vertex, 5)
    edg2 = random.sample(vertex, 5)

    randomize(edg1, edg2)

    while not is_strongly_connected(graph):
        randomize(edg1, edg2)

