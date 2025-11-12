def dfs_euler_cycle(u, graph, cycle):
    for v in range(len(graph)):
        if graph[u][v]:
            graph[u][v] = 0
            graph[v][u] = 0
            dfs_euler_cycle(v, graph, cycle)
    cycle.append(u)
    return cycle

def List_to_Matrix(G):
    n = len(G)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for v in G[i]:
            matrix[i][v] = 1
    return matrix

g = [[1,2],
     [0,2,3,4,5,6],
     [1,3,4],
     [0,1,4,5],
     [1,2,3,5],
     [3,4],
]

g1 = List_to_Matrix(g)
print(dfs_euler_cycle(0,g1,[]))
