#Traktuje punkty jako wierzcholki grafu
#Nastepnie sprawdzam czy mozna przejsc od x do y:
#Jesli mozna, napewno mozna scalic przedzialy aby utworzyly x i y
#Nastepnie musimy policzyc ile jest takich przedzialow
#Do tego potrzebujemy przejsc po kazdej krawedzi i sprawdzic
#czy lezy na sciezce od x do y, jesli tak oznacza ze nalezy ja dodac do rozwiazania



from zad1testy import runtests
from collections import deque
from math import inf


def intuse( I, x, y ):
    n = max(max(x,y) for x ,y in I) + 1
    if y >= n:
        return []
    g_from_x = [[] for _ in range(n)]
    g_from_y = [[] for _ in range(n)]
    for u,v in I:
        g_from_x[u].append(v)
        g_from_y[v].append(u)
    from_start = bfs(g_from_x,x)
    from_end = bfs(g_from_y,y)
    path = []
    for i in range (len(I)):
        u = I[i][0]
        v = I[i][1]
        # gdy krawedz u,v lezy na najkrotszej sciezce wtedy jest to odpowiedz
        if from_start[u] and from_end[v]:
            path.append(i)
    return path

def bfs(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    Q = deque()
    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)
    return visited

runtests( intuse )


