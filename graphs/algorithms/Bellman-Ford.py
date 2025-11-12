from math import inf

G = [[(1, 3), (2, 1), (4, 2)],
     [(0, 3), (2, 5)],
     [(1, 5), (0, 1), (3, 6)],
     [(2, 6), (4, 4)],
     [(3, 4), (0, 2)]]


def bellman_ford(G, s):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    for i in range(n-1):
        for v in range(n):
            for u,w in G[v]:
                if d[u] > d[v] + w:
                    d[u] = d[v] + w
                    parent[u] = v

    #weryfikacja
    for v in range(n):
        for u,w in G[v]:
            if d[u] > d[v] + w:
                return False

    return d

print(bellman_ford(G,0))
