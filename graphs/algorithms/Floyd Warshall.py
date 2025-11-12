from math import inf

G = [
    [0, 3, inf, 5],
    [2, 0, inf, 4],
    [inf, 1, 0, inf],
    [inf, inf, 2, 0]
]

def Floyd_war(G):
    n = len(G)
    for k in range(n):
        for u in range(n):
            for v in range(n):
                    G[u][v] = min(G[u][v],G[u][k]+G[k][v])
    print(G)

Floyd_war(G)