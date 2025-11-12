from collections import deque
from math import inf

E = [(1, 5, 10), (4, 6, 12), (3, 2, 8), (2, 4, 4), (2, 0, 10), (1, 4, 5), (1, 0, 6), (5, 6, 8), (6, 3, 9)]
def edges_to_graph(E):
    n = 0
    for u,v,w in E:
        n = max(n,u,v)
    G = [[] for _ in range(n+1)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    return G

def bfs_weight(G,s):
    n = len(G)
    d = [inf] * n
    d[s] = 0
    q = deque()
    q.append((s,0,0))
    while q:
        v, dist,delay = q.popleft()
        #dodaj wage pomniejszona o 1 do kolejki
        if delay > 0:
            q.append((v,dist,delay-1))
        else:
            #dist jest rowne 0 wiec odwiedzam wierczholek
            for u,w in G[v]:
                if d[u] > dist + w:
                    d[u] = dist + w
                    q.append((u,dist+w,w))
    return d

G = edges_to_graph(E)
print(bfs_weight(G,0))







