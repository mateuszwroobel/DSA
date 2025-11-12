from collections import deque
from math import inf

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
            if graph[i][j] == 1:
                N[i].append(j)
    return N

#bfs on adj_list
def bfs_list(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for  _ in range(n)]
    d = [inf for _ in range(n)]
    Q = deque()
    d[s] = 0
    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)
    return d

print(bfs_list(graph,0))

#bfs on matrix
def bfs_matrix(g,s):
    inf = float('inf')
    n = len(g)
    visited = [False for _ in range(n)]
    d = [inf for _ in range(n)]
    q = deque()
    visited[s] = True
    d[s] = 0
    q.append(s)
    while q:
        v = q.popleft()
        for u in range(n):
            if g[v][u] == 1 and not visited[u]:
                d[u] = d[v] + 1
                visited[u] = True
                q.append(u)
    return d

print(bfs_matrix(graph,0))
