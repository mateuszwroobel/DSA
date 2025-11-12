from egz3atesty import runtests
from math import inf
from collections import deque

#O(V(V+E)) = O(VE)
def mykoryza(G, T, d):
    n = len(G)
    k = len(T)
    cnt = 0
    infected = [[] for _ in range(k)]
    for i in range(k):
        infected[i] = bfs(G,T[i])
    final_infections = [[inf,None] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            if infected[j][i] < final_infections[i][0]:
                final_infections[i][0] = infected[j][i]
                final_infections[i][1] = j
            elif infected[j][i] == final_infections[i][0]:
                final_infections[i][1] = min(j, final_infections[i][1])
        if  final_infections[i][1] == d:
            cnt += 1
    return cnt

def bfs(G,s):
    n = len(G)
    d = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s]= 0
    visited[s] = True
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        for u in G[v]:
            if not visited[u]:
                d[u] = d[v] +1
                visited[u] = True
                q.append(u)
    return d


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(mykoryza, all_tests=True)
