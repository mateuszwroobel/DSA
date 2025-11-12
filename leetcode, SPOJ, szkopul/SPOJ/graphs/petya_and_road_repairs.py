def repairs(E,milkman):
    #rozwiazanie sprowadza sie do znalezienia minimalnego drzewa rozpinajacego ale z dodatkowymi warunkami
    #nie bierzemy pod uwage polaczen miedzy mleczarzami, one nie sa nam potrzebne bo tylko wydluzaja sciezke
    #dowod: jezeli mleczarze v,k aktualny wierzcholek u
    #jezeli chcemy dojsc z u do v lub k ktorzy sa mleczarzami, to idziemy do najlbliszego i sciezka miedzy nimi
    #nie jest nam potrzebna
    #Wykonujemy, az polaczaymy nie wszystkie wierzcholki, tylko wierzcholki bez mleczarzy

    class node:
        def __init__(self,value):
            self.parent = self
            self.rank = 0
            self.value = value

    def find(x):
        if x.parent != x:
            x.parent = find(x.parent)
        return x.parent

    def union(x,y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank+=1
        return True

    def sort_edges(E,milksman):
        _E = []
        for u,v,w in E:
            if milksman[u] == 1 and milksman[v] == 1:
                continue
            _E.append((u,v,w))

        _E = sorted(_E, key = lambda x: x[2])
        return _E

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

    def kruskal(G,E,milksman):
        _E = sort_edges(E,milkman)
        n = len(G)
        mst_cost = []
        nodes = [node(i) for i in range(n)]
        for u,v,w in _E:
            if union(nodes[u],nodes[v]):
                mst_cost.append(w)
            if len(mst_cost) == n - sum(milksman):
                return sum(mst_cost)
        return -1

    G = edge_to_adj(E)

    return kruskal(G,E,milkman)


milkmen = [0, 1, 0, 1, 0]

edges = [
    (0, 1, 11),
    (0, 2, 1),
    (0, 4, 17),
    (1, 2, 1),
    (2, 3, 18),
    (3, 4, 3),
    (1, 3, 5)
]

print(repairs(edges,milkmen))