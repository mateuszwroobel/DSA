from math import inf
from egz3btesty import runtests

def maze(L):
    n = len(L)
    dp = [[-inf for _ in range(n)] for _ in range(n)]
    left = [[0 for _ in range(n)] for _ in range(n)]
    right = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(1,n):
        if L[0][i-1] == ".":
            dp[0][i] = dp[0][i-1] + 1


    for i in range(1,n):

        left[i][0] = left[i-1][0]
        for j in range(n):
            from_left = -inf
            if L[i][j] == ".":
                #ile komnat moge przejsc z lewej
                from_left = left[i][j-1] + 1
            from_down = -inf
            if L[i][j] == ".":
                from_up = dp[i-1][j]
            left[i][j] = max(from_left,from_up)

        right[i][n-1] = right[i-1][n-1]
        for j in range(n-2,-1,-1):
            from_up = -inf
            if L[i][j] == ".":
                # ile komnat moge przejsc z lewej
                from_left = right[i][j + 1] + 1
            from_upp = -inf
            if L[i][j]== ".":
                from_upp = dp[i - 1][j]
            right[i][j] = max(from_right, from_upp)
        for j in range(n):
            dp[i][j] = max(right[i][j], left[i][j]) + 1

    return dp[n-1][n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=False)
