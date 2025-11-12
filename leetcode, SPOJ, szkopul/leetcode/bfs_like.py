#924
from collections import deque
from math import inf

def malware_spread(graph,initial):
    def bfs(g, inactive, initial):
        n = len(g)
        infected_by = [-1 for _ in range(n)]
        q = deque()
        infected = 0
        for id, v in enumerate(initial):
            if v != inactive:
                infected_by[v] = id
                q.append((id, v))
                infected += 1
        while q:
            id, v = q.popleft()
            for u in range(n):
                if g[v][u] == 1 and infected_by[u] == -1:
                    infected_by[u] = id
                    infected += 1
                    q.append((id, u))
        return n - infected
    # we want to minimize healthy so remove initial which cause the most infections
    k = len(initial)
    initial.sort()
    num_of_healthy= [0] * k
    best = -inf
    ind = None
    for v in range(k):
        num_of_healthy[v] = bfs(graph, initial[v], initial)
        if num_of_healthy[v] > best:
            best = num_of_healthy[v]
            ind = initial[v]

    return ind

graph = [[1,0,0,0,1,0,0,0,0,0,1],[0,1,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0,0,0],[0,1,0,1,0,1,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,1,1,0],[0,0,0,0,0,0,1,1,0,0,0],[0,0,1,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,0,1]]
initial = [7,8,6,2,3]

#1298
def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
    q = deque()
    n = len(status)
    visited = [False for _ in range(n)]
    total = 0
    have_key = {}
    have_box = {} #boxy ktore mamy
    for box in initialBoxes:
        #czy wgl otwarte jest pudelko initial
        if status[box] == 1:
            total += candies[box]
            for key in keys[box]:
                if not key in have_key:
                    have_key[key] = True
            for b in containedBoxes[box]:
                if not b in have_box:
                    have_box[b] = True
                if status[b] == 1 or b in have_key:
                    visited[b] = True
                    q.append(b)
        else:
            if not box in have_box:
                have_box[box] = True
    while q:
        box = q.popleft()
        total += candies[box]

        #zbieranie kluczy i sprawdzanie czy juz mozna zebrac jakies czekoladki
        for key in keys[box]:
            if not key in have_key:
                have_key[key] = True
            if key in have_key and key in have_box and not visited[key]:
                visited[key] = True
                q.append(key)


        #analogicznie jak z kluczami
        for b in containedBoxes[box]:
            if not b in have_box:
                have_box[b] = True
            if (b in have_key and b in have_box and not visited[b]) or (status[b] == 1):
                visited[b] = True
                q.append(b)
    return total

status = [1,0,1,0]
candies =[7,5,4,100]
keys =[[],[],[1],[]]
containedBoxes =[[1,2],[3],[],[]]
initialBoxes =[0]

print(maxCandies(status,candies,keys,containedBoxes,initialBoxes))


