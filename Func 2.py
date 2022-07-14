
adj_list={
    "Dushanbe":["Vaduz","Bamako","Podgorica","Sofia"],
    "Podgorica":["Sofia"],
    "Vaduz":["Bamako","Podgorica","Sofia"],
    "Bamako":["Podgorica","Sofia"],
    "Sofia":[]
    
}
color={}
parent={}

for u in adj_list.keys():
    color[u]='W'
    parent[u]=None

#perform dfs to determine whether graph is cyclic
def dfs(u,color,parent):
    color [u]='G'
    for v in adj_list[u]:
        if color [v]=='W':
            cycle=dfs(v,color,parent)
            if cycle==True :
                return True
        elif color[v]=='G':
            print("Cycle Found",u,v)
            return True
    color[u]='B'
    return False
#call an function to add the edges if it is not cyclic
  
is_cyclic = False
for u in adj_list.keys():
    if color[u]=='W':
         if_cyclic=dfs(u,color,parent)
         if if_cyclic == True:
             break
print("Is Cyclic",is_cyclic)

