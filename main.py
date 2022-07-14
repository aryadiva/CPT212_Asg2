import func4
import init
from func1 import is_strongly_connected

vertex = init.vertex;
edges = init.edges;
dist = init.dist;

## This file is for the main menu or main UI
...

## looping through a list of distance to find the correct distance
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


# user inputting new edges -----------
while True:
    init.draw_graph()
    n = input("Please input the starting vertex: ")
    i=0
    while i <= len(vertex):
        temp = vertex[i]
        if(temp == n):
            break
        i+=1
        if(i == 5 and temp != n):
            print("Unknown input, terminating...")
            quit()

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
    i=0

    add(n, m);
    init.draw_graph()
    func4.mstt()
    print("Add more? y/n")
    q = input()
    if(q == "n"):
        break
    if(q == "y"):
        continue
    if(q != "n" and q != "y"):
        print("Not a valid response, exiting...")
        quit()
        ...
#---------------------------------------
