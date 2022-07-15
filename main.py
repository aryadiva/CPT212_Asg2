import common_func
import func1
import func3
import func4
import init
from common_func import add
from common_func import add_edge
from common_func import remove_edges
from common_func import reset
from func1 import is_strongly_connected
from func1 import generate_strongly_connected_graph


graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

## This file is for the main menu or main UI
def main_menu():
    init.draw_graph_init()
    print('###################################\n'
        '|            Main Menu            |\n'
        '###################################\n'
        '|  1. Add Edge                    |\n'
        '|  2. Remove Edge                 |\n'
        '|  3. Check Connectivity Graph    |\n'
        '|  4. Check Cyclic Graph          |\n'
        '|  5. Calculate Shortest Path     |\n'
        '|  6. Show Minimum Spanning Tree  |\n'
        '|  7. Reset Graph                 |\n'
        '|  8. Exit                        |\n'
        '####################################')

def options():
    while True:
        c = input("\nPick an option: \n")
        if (c == '1'):
            add_edge()
        if (c == '2'):
            remove_edges()
        if (c == '3'):
            if func1.is_strongly_connected(graph):
                print("The graph is strongly connected")
            else:
                print("The graph is not strongly connected")
                func1.generate_strongly_connected_graph(graph)
                reset()
        if (c == '4'):
            None
            # func2
        if (c == '5'):
            StartingPoint=common_func.FetchStart()
            EndingPoint=common_func.FetchEnd()
            ShortestPath=func3.shortest_path(graph, init.vertex[StartingPoint], init.vertex[EndingPoint])
            print(ShortestPath)
            reset()
        if (c == '6'):
            func4.mst()
            a = input("Do you wish to generate randomized minimum spanning tree? y/n\n")
            if(a == 'y'):
                func4.random_mst()
                func4.mst()
            else:
                continue
        if (c == '7'):
            reset()
        if (c == '8'):
            quit()

main_menu()
options()

