import networkx as nx
from matplotlib import pyplot as plt
import init

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

def spa(self, src):
    dist = [1e7] * self.V
    dist[src] = 0
    sptSet = [False] * self.V

    for cout in range(self.V):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = self.minDistance(dist, sptSet)

        # Put the minimum distance vertex in the
        # shortest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shortest path tree
        for v in range(self.V):
            if (self.graph[u][v] > 0 and
                    sptSet[v] == False and
                    dist[v] > dist[u] + self.graph[u][v]):
                dist[v] = dist[u] + self.graph[u][v]

    self.printSolution(dist)