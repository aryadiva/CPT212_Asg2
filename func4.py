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
    nx.draw_networkx(T, with_labels=True, node_size=1500, node_color='grey', edge_color='grey', arrowsize=22,
                     font_size=16)
    ax = plt.gca()
    ax.margins(0.005)
    plt.axis("off")
    plt.show();

# function for validating user input to minimum spanning tree
def min_ST():
    while True:
        while True:
            n = input("Please input the starting vertex: ")
            i = 0
            while i <= len(vertex):
                temp = vertex[i]
                if (temp == n):
                    break
                i += 1
                if (i == 5 and temp != n):
                    print("Unknown input, terminating...")
                    quit()
            break

        while True:
            m = input("Please input the destination vertex: ")
            i = 0
            while i <= len(vertex):
                temp = vertex[i]
                if (temp == m):
                    break
                i += 1
                if (i == 5 and temp != m):
                    print("Unknown input, terminating...")
                    quit()
            i = 0
            break

        add(n, m);
        init.draw_graph_init()
        mst()
        print("Add more? y/n")
        q = input()
        if (q == "n"):
            quit()
        if (q == "y"):
            continue
        if (q != "n" and q != "y"):
            print("Not a valid response, exiting...")
            quit()

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



