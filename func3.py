import networkx as nx
import init
import random

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

# shortest path between the vertices
def shortest_path(graph, start, end):
    # if there is no edge between two vertices, random generate until the path is found
    while not nx.has_path(graph, start, end):
        a = random.choice(init.vertex)
        b = random.choice(init.vertex)
        if graph.has_edge(a, b) and not graph.has_edge(b, a):
            continue
        if a != b:
            graph.add_edge(a, b, weight=init.weight_dicts[a + b])
    return nx.shortest_path(graph, start, end)

"""
start = input("The Starting Point: ")
StartingPoint = common_func.FetchVertex(start)
end = input("The Ending Point: ")
EndingPoint = common_func.FetchVertex(end)
ShortestPath = func3.shortest_path(graph, init.vertex[StartingPoint], init.vertex[EndingPoint])
print(ShortestPath)



def FetchVertex(a):
    if(a == 'BA'):
        return 0
    elif(a == 'VA'):
        return 1
    elif(a == 'PO'):
        return 2
    elif(a == 'SO'):
        return 3
    elif(a == 'DU'):
        return 4
"""