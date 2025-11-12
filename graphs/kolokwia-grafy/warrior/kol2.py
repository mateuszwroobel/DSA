from kol2testy import runtests
from queue import PriorityQueue
from math import inf

def warrior(G, s, t):
    g = edge_to_adj(G)
    d = modified_dijkstra(g, s, t)
    return d

def modified_dijkstra(G, s, t):
    n = len(G)
    # np d[v][k] najwczesniejszy czas/najmn odlg z jakim podroznik dotarl do miasta v bedac dokladnie k godzin bez snu
    d = [[inf] * 17 for _ in range(n)]
    q = PriorityQueue()
    q.put((0, s, 0))  # time,v,awake
    d[s][0] = 0
    sleep = 8

    while not q.empty():
        time, v, awake = q.get()
        if v == t:
            return time
        if time > d[v][awake]:
            continue
        for u, w in G[v]:
            if awake + w > 16:
                if d[u][w] > d[v][awake] + w + sleep:
                    d[u][w] = d[v][awake] + w + sleep
                    q.put((d[u][w], u, w))

            if awake + w <= 16:
                if d[u][awake + w] > d[v][awake] + w:
                    d[u][awake + w] = d[v][awake] + w
                    q.put((time + w, u, awake + w))
    return -1

def edge_to_adj(E):
    # N - number of vertexes
    N = 0
    for u, v, w in E:
        N = max(N, u + 1, v + 1)

    G = [[] for i in range(N)]
    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))
    return G


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests=True)
