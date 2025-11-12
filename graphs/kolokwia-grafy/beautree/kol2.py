from kol2testy import runtests


class Node:
    def __init__(self, val):
        self.parent = self
        self.rank = 0
        self.val = val


def beautree(G):
    def find(x):
        if x != x.parent:
            x.parent = find(x.parent)
        return x.parent

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1
        return True
    def edgyfi(graph):
        edges = []
        for u in range(len(G)):
            for (v, w) in G[u]:
                if u < v:
                    edges.append([u, v, w])
        return edges

    def BT(graph):
        E = edgyfi(graph)
        E.sort(key=lambda x: x[2])
        BT = []
        m = 0
        while m <= len(E):
            V = []
            for i in range(len(graph)):
                V.append(Node(i))
            for i in range(m, len(E)):
                v = E[i][0]
                u = E[i][1]
                if union(V[v],V[u]):
                    BT.append(E[i])
                    if len(BT) == len(graph) - 1:
                        return sum(x[2] for x in BT)
                else:
                    BT = []
                    m += 1
                    break
        return None

    return BT(G)


runtests(beautree, all_tests=True)