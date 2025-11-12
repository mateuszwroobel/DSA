from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

#bipartite/BFS/list of neighbours

G = [[2,3,4],
     [3,4],
     [0],
     [0,1],
     [0,1],
]

#checking if graph is bipartite using BFS
def is_bipartite(G):
    n = len(G)
    visited = [False for _ in range(n)]
    color = [0 for _ in range(n)]
    q = deque()
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            q.append(i)

            while q:
                u = q.popleft()
                #print(f"Biore z kolejki: {u}")
                for v in G[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 1 - color[u]
                        #print(color)
                        q.append(v)
                        #print(q, f"V:{v}, u(wziety z kolejki):{u}")
                    elif visited[v] and color[v] == color[u]:
                        #print("jestem w elif", f"V:{v},u(wziety z kolejki):{u}")
                        return False
    return True

#is_bipartite(G)

g1 =[[1,8],
     [0,2,3,5,6,7],
     [1],
     [1,4,5],
     [3],
     [3],
     [1],
     [1],
     [0,9],
     [8]
]

g2 = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]

# G = nx.Graph()
# for u,neighbors in enumerate(g2):
#     for v in neighbors:
#         G.add_edge(u,v)
#
# pos = nx.spring_layout(G,seed = 50)
# plt.figure(figsize=(8,6))
# nx.draw(G, pos,
#         with_labels=True,
#         node_size=800)
# plt.show()

print(is_bipartite(g2))