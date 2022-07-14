import networkx as nx

import init
import func4
import func3

vertex = init.vertex;
edges = init.edges;
dist = init.dist;
graph = nx.DiGraph()

# looping through a list of distance to find the correct distance
def dist_loop(j, k):
    temp1 = (j+'_'+k)
    temp2 = (k+'_'+j)
    i = 0;
    while i < 10:
        if (temp1 == dist[i][0]):
            result = dist[i][1];
        if (temp2 == dist[i][0]):
            result = dist[i][1];
        i+=1;
    return result

# Add edges function
def add(a, b):
    for x in vertex:
        if(x == a):
            a = x;
        if(x == b):
            b = x;
            dist = dist_loop(a, b)
            edges.append((a,b,dist))
            break;

# Remove edges function
def remove_edges(a, b) :
  if(init.graph.has_edge(a, b) == True) :
    init.graph.remove_edge(a, b)
    print('The edge has been removed')
  else :
    print('The edge to be removed does not exist')

# user removing edges
while True:
    init.draw_graph()
    print("Please input the starting vertex: ")
    n = input()
    print("Please input the destination vertex: ")
    m = input()

    remove_edges(n, m);
    init.draw_graph()
    print("Remove more? y/n")
    q = input()
    if(q == "n"):
        break;

# user inputting new edges -----------
while True:
    init.draw_graph()
    print("Please input the starting vertex: ")
    n = input()
    print("Please input the destination vertex: ")
    m = input()

    add(n, m);
    init.draw_graph()
    func4.mstt()
    print("Add more? y/n")
    q = input()
    if(q == "n"):
        break;
#---------------------------------------

