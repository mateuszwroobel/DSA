#implementation of finding bridges using Tarjan Algorithm
def find_bridge(G):
    n = len(G)
    inf = float('inf')
    time = 0
    visited = [False for _ in range(n)]
    low = [inf for _ in range(n)]
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    bridges = []

    def dfs_visit(G,v):
        nonlocal time,d
        time+=1
        visited[v] = True
        d[v] = time
        low[v] = time
        for u in G[v]:     #v-parent, u-child
            if not visited[u]:
                parent[u] = v
                dfs_visit(G,u)
                low[v] = min(low[v],low[u])
            elif visited[u] and (u!=parent[v]): #back edge
                low[v] = min(low[v],d[u])
        if low[v] == d[v] and parent[v] is not None:
            bridges.append((v,parent[v]))

    for v in range(n):
        if not visited[v]:
            dfs_visit(G,v)
    #print(d)
    return bridges

g = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
# #g=[[1,6],
#      [0,2],
#      [1,3,6],
#      [2,4,5],
#      [3,5],
#      [3,4],
#     [0,2]
# ]
print(find_bridge(g))

