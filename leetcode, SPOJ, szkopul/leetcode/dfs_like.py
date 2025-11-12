#2477
'''
Algorytm opiera sie na nastepujacym pomysle. Do rozwiazania wykorzystuje
algorytm dfs i bfs.
Bfs jest potrzebny, aby okreslic odleglosci do wierzcholka 0.
Dfs bede uruchamial od najdalszych wierzcholkow, aby "zabierac" po drodze
pasazerow z innych "miast".
Uruchamiam algorytm, a nastepnie sledze sciezke od danego wierzcholka,
Jesli odwiedzam nastepny wierczholek i mam miejsce w samochodzie to
zabieram ze soba nastepny wierzcholek.
Koncze dana sciezke gdy dotre do wierzcholka 0
'''

def minimumFuelCost(roads, seats):
    inf = float('inf')

    def create_graph(roads):
        n = max(max(u, v) for u, v in roads) + 1
        G = [[] for _ in range(n)]
        for u,v in roads:
            G[u].append(v)
            G[v].append(u)
        return G

    G = create_graph(roads)

    def dfs(G, seats):
        n = len(G)
        visited = [False for _ in range(n)]
        total_fuel = 0

        def dfs_visit(G, v, seats):
            nonlocal visited, total_fuel
            visited[v] = True
            people = 1
            for u in G[v]:
                if not visited[u]:
                    dfs_visit(G, u,seats)
                    #licze liczbe dzieci w podrzewie
                    sub_people = dfs_visit(G,u,seats)
                    trips = (people + seats - 1) // seats
                    people+=sub_people

            return people
        dfs_visit(G, 0, seats)
        return total_fuel

    return dfs(G,seats)
    # def bfs(G,s):
    #     n = len(G)
    #     d = [inf for _ in range(n)]
    #     visited= [False for _ in range(n)]
    #     q = deque()
    #     q.append(s)
    #     d[s] = 0
    #     visited[s] = True
    #     while q:
    #         v = q.popleft()
    #         for u in G[v]:
    #             if not visited[u]:
    #                 visited[u] = True
    #                 d[u] = d[v] + 1
    #                 q.append(u)
    #     return d

    #Sortowanie wierzcholkow za pomoca count_sorta
    # def count_sort(d):
    #     n = len(d)
    #     k = max(d)
    #     for ind,dist in enumerate(d):
    #         d[ind] = dist,ind
    #     B = [0] * n
    #     C = [0] * (k+1)
    #     for i in range(n):
    #         C[d[i][0]] += 1
    #     for i in range(k-1,-1,-1):
    #         #ile jest liczb wiekszych badz rownych niz "i"
    #         C[i] = C[i] + C[i+1]
    #     for i in range(n):
    #         C[d[i][0]] -= 1
    #         B[C[d[i][0]]] = d[i][1]
    #
    #     for i in range(n):
    #         d[i] = B[i]
    #     #tablica d zawiera indeksy, ktore maja najdluzszy dystans
    #     return d

