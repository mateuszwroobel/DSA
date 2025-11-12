#Euler cycle in undirected graph represented by list of adjacency.
#We assume graph is connected and deg of every vertex is even.
#This implementation include "deleting" edges in O(1) time. This is the main focus of this algorithm.
#Every edge will have reference to True/False object. It leads to reducing time complexity.


class Flag:
     def __init__(self):
          self.val = False

     def __str__(self):
          return f"{self.val}"

     def __eq__(self, other):
          if isinstance(other,bool):
               return self.val == other
          return False

def add_edge(edge_flags, u,v):
     key = tuple(sorted((u,v)))
     if key not in edge_flags: #edge_flags is dict, "if in" function is O(1) using dict
          edge_flags[key] = Flag()

def is_active(edge_flags,u,v):
     key = tuple(sorted((u,v)))
     return edge_flags[key]

def euler(G):
     n = len(G)
     edge_flag = {}
     cycle = []
     #adding flags
     for u in range(n):
          for v in G[u]:
               add_edge(edge_flag,u,v)

     def dfs_visit(G,v,key):
          edge_flag[key] = True
          for u in G[v]:
               key = tuple(sorted((v,u)))
               if edge_flag[key] == False:
                    dfs_visit(G,u,key)
          cycle.append(v)

     for u in range(n):
          for v in G[u]:
               key = tuple(sorted((v, u)))
               if edge_flag[key] == False:
                    dfs_visit(G,v,key)
     return cycle


g = [[1,3],
     [0,2,3,4],
     [1,3,4],
     [0,1,4,5],
     [1,2,3,5],
     [3,4],
]
print(euler(g))

