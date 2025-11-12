#Mateusz Wróbel
#Do rozwiazania stosuje algorytm zmodyfikowany BFS, ktory nie pozwoli mi wychodzic z wierzcholka, tam gdzie sa Szpiedzy.
#Dzieki temu sprawdzam, czy idac od krola do krolowej, bede mogl sie dostac omijajac zablokowany wierzcholek
#Jesli droga od krola do krolowej nie istnieje bez zabronionego wierzcholka, oznacza to, że nie dostarczymy informacji o
#kocie. Dla kazdego dnia uruchamiam BFS, wiec zlozonosc czasowa wynosi O(D(V+E)).

from egz2Atesty import runtests
from collections import deque


def kingnqueen(V, E, D, K, Q, B):
    def create_graph(V,E):
        G = [[] for _ in range(V)]
        for u,v in E:
            G[u].append(v)
            G[v].append(u)
        return G

    def bfs(G,s,t,inactive_vertex):
        n = len(G)
        visited = [False] * n
        visited[s] = True
        q = deque()
        q.append(s)

        while q:
            v = q.popleft()
            #pomijanie zabronionego wierzcholka
            if v == inactive_vertex:
                continue
            if v == t:
                return True

            for u in G[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)
        return False

    G = create_graph(V,E)
    cnt = 0
    for i in range(D):
        inactive = B[i]
        king = K[i]
        queen = Q[i]
        cnt += bfs(G,king,queen,inactive)

    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kingnqueen, all_tests=True)
