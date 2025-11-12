#G - graph represented by list of adjacency
def topological_sort(G):
    n = len(G)
    visited = [False for i in range(n)]
    time = 0
    T = []
    def DFS_Visit(G,v):
        nonlocal time
        visited[v] = True
        time+=1
        for u in G[v]:
            if not visited[u]:
                DFS_Visit(G,u)
        T.append(v)
        time+=1
    for v in range(n):
        if not visited[v]:
            DFS_Visit(G,v)
    return T[::-1]


g2 = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]

print(topological_sort(g2))