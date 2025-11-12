import heapq
from egz2Btesty import runtests

def bitgame(T):
    heap = []
    heapq.heappush(heap, T[0])
    n = len(T)

    for i in range(1,n):
        collision = False
        while heap and heap[0] <= T[i]:
            heapq.heappop(heap)
            collision = True
        if not collision:
            heapq.heappush(heap, T[i])

    return len(heap)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(bitgame, all_tests=True)
