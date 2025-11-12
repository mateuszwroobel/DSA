from egz3atesty import runtests
from math import inf
from collections import deque

#O(V(V+E)) = O(VE)
#multiple BFS
def mykoryza(G, T, d):
    return bfs(G,T,d)

def bfs(G,T,ans):
    n = len(G)
    d = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    infected_by = [None for _ in range(n)]
    q = deque()
    cnt = 1
    #dodaje pierwsze grzyby do kolejki
    for i,mushroom in enumerate(T):
        q.append((mushroom,i))
        infected_by[mushroom] = i
        visited[mushroom] = True
        d[mushroom] = 0

    while q:
        v, infected = q.popleft()
        for u in G[v]:
            if not visited[u]:
                d[u] = d[v] + 1
                infected_by[u] = infected
                visited[u] = True
                q.append((u,infected))
                if infected == ans:
                    cnt+=1
            else:
                #juz bylem, w tym grzybie ale maksymalnie 1 krawedz wczesniej,
                #wiec musze wybrac mniejszy indeks
                if d[u] == d[v] + 1:
                    if infected_by[u] > infected:
                        infected_by[u] = infected
                        if infected_by[u] == ans:
                            cnt+=1
    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(mykoryza, all_tests=True)
