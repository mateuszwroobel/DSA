from collections import deque
import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N, R, M = map(int, read().split())
    graph = [[] for _ in range(N)]
    for _ in range(R):
        a, b = map(int, read().split())
        #przesuniecie bo indeksowanie jest od 1
        a-=1
        b-=1
        graph[a].append(b)
        graph[b].append(a)

    soldiers = []
    for _ in range(M):
        K, S = map(int, read().split())
        soldiers.append((K-1, S))

    def multi_source_bfs(sources,n,G):
        visited_by = [-1] * n
        q = deque()
        for index, (s, reach) in enumerate(sources):
            q.append((reach-1,s,index))
            visited_by[s] = index
        while q:
            r, v, id = q.popleft()
            #pomin jesli r < 0
            if r < 0:
                continue
            for u in G[v]:
                if visited_by[u] == -1:
                    visited_by[u] = id
                    q.append((r-1,u,id))
                elif visited_by[u] != id:
                    return False
        for city in visited_by:
            if city == -1:
                return False
        return True

    if multi_source_bfs(soldiers,N,graph):
        print("Yes")
    else:
        print("No")
