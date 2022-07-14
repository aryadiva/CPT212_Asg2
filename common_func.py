import init

vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

## looping through a list of distance to find the correct distance
def dist_loop(j, k):
    temp1 = (j+k)
    for x in dist:
        if(temp1 == x):
            result = dist[x]
    return result

# Add function
def add(a, b):
    for x in vertex:
        if(x == a):
            a = x;
        if(x == b):
            b = x;
            dist = dist_loop(a, b)
            edges.append((a,b,dist))
            break;
# add edge function
def add_edge():
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
    add(n,m)

# user removing edges
while True:
    init.draw_graph()
    print("Please input the starting vertex: ")
    n = input()
    print("Please input the destination vertex: ")
    m = input()

    if (init.graph.has_edge(n, m) == True):
        init.graph.remove_edge(n, m)
        print('The edge has been removed')
    else:
        print('The edge to be removed does not exist')
    init.draw_graph()
    print("Remove more? y/n")
    q = input()
    if(q == "n"):
        break;