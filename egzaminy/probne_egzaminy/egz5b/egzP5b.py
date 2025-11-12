from egzP5btesty import runtests 

def koleje ( B ):
    def create_graph(B):
        n = max(max(x,y) for x,y in B) + 1
        G = [[] for _ in range(n)]
        for u,v in B:
            if v not in G[u]:
                G[u].append(v)
            if u not in G[v]:
                G[v].append(u)

        return G
    G = create_graph(B)

    def find_articulation_points(G):
        n = len(G)
        inf = float('inf')
        time = 0
        visited = [False] * n
        low = [inf] * n
        d = [inf] * n
        parent = [None] * n
        articulation = [False] * n

        def dfs_visit(v):
            nonlocal time
            time += 1
            visited[v] = True
            d[v] = low[v] = time
            children = 0

            for u in G[v]:
                if not visited[u]:
                    parent[u] = v
                    children += 1
                    dfs_visit(u)
                    low[v] = min(low[v], low[u])

                    if parent[v] is None and children > 1:
                        articulation[v] = True
                    if parent[v] is not None and low[u] >= d[v]:
                        articulation[v] = True
                elif u != parent[v]:
                    low[v] = min(low[v], d[u])

        for v in range(n):
            if not visited[v]:
                dfs_visit(v)

        cnt = 0
        for v in articulation:
            if v:
                cnt+=1
        return cnt
    return find_articulation_points(G)

runtests ( koleje, all_tests=True)