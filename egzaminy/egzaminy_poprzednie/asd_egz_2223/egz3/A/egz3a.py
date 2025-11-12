from egz3atesty import runtests
from math import inf
from collections import deque


def goodknight(G, s, t):
    g = matrix_to_adj(G)
    n = len(G)
    d = [[inf] * 17 for _ in range(n)]
    q = deque()
    sleep = 8
    d[s][0] = 0
    q.append((0,s,0,0)) #v,awake
    while q:
        time,v, awake,delay = q.popleft()
        #dodaj do kolejki opoznienie -1
        if delay > 0:
            q.append((time,v,awake,delay-1))
            continue
        if time > d[v][awake]:
             continue
        if v == t:
            return time
        #Wchodzimy do wierzcholka, delay == 0
        for u,w in g[v]:
            #trzeba spac
            if awake + w > 16:
                new_time = time + sleep + w
                if d[u][w] > new_time:
                    d[u][w] = new_time
                    q.append((new_time,u,w,new_time))
            else:
                new_time = time + w
                awake_after_trip = awake + w
                if d[u][awake_after_trip] > new_time:
                    d[u][awake_after_trip] = new_time
                    q.append((new_time, u, awake_after_trip, new_time))

    return min(d[t])

#O(n^2)
def matrix_to_adj(G):
    n = len(G)
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                g[i].append((j,G[i][j]))
    return g

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests=True)
