graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0]
]


def Matrix_to_list_of_neighbors(g):
    k = len(g)  # number of V
    N = [[] for i in range(k)]  # Neighbors
    for i in range(k):
        for j in range(k):
            if g[i][j] == 1:
                N[i].append(j)
    return N

def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0
    def DFSvisit(G, v):
        nonlocal time
        visited[v] = True
        time+=1
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                DFSvisit(G,u)
        time +=1

    for v in range(n):
        if not visited[v]:
            DFSvisit(G,v)
