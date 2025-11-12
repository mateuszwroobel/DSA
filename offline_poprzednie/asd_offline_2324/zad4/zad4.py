from zad4testy import runtests
from collections import  deque
from math import inf

def create_graph(L,t):
    n = 0
    for u,v,p in L:
        n = max(n,v+1,u+1)
    G = [[]for _ in range(n)]
    for u,v,p in L:
        G[u].append((v,p-t,p+t))
        G[v].append((u,p-t,p+t))
    return G

def Flight(L, x, y, t):
    G = create_graph(L,t)
    return bfs(G,x,y)

def bfs(G,s,t):
    n = len(G)
    visited =[False for _ in range(n)]#odwiedzamy gdy zgadza sie pulap
    parent = [None for _ in range(n)]
    q = deque()
    visited[s] = True
    q.append((s,-inf,inf))
    while q:
        v, p1, p2 = q.popleft()
        for u,low,high in G[v]:
            if not visited[u]:
               # print(v, p1, p2, u, low, high)
                if (p1 <= low <= p2) or   p1 <= high <= p2:
                    new_high = min(high,p2)
                    new_low = max(low,p1)
                    #print("new:" ,new_low, new_high)
                    q.append((u,new_low,new_high))
                    visited[u] = True
    if visited[t]:
        return True
    else:
        return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests=True)