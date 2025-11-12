from email.policy import default

from kol2btesty import runtests
from math import inf


def min_cost(O, C, T, L):
    #preparing data
    A  = [(0,0)]
    for i in range(len(C)):
        A.append((O[i],C[i]))
    A.append((L,0))
    A.sort()
    n = len(A)
    dp = [[inf for _ in range(2)] for _ in range(n)]
    #base case
    dp[n-1][0] = 0
    dp[n-1][1] = 0

    def reku(i,exception_used):
        if i >= n: return inf
        if dp[i][exception_used] != inf: return dp[i][exception_used]
        cost = A[i][1]
        min_future_cost = inf
        if exception_used:
            possible_cost = min((reku(j,1) + cost for j in range(i+1,n) if A[j][0] - A[i][0] <= T), default = inf)
            min_future_cost = possible_cost
        else:
            cost_normal = min((reku(j,0) + cost for j in range(i+1,n) if A[j][0] - A[i][0] <= T), default = inf)
            cost_expection_drive = min((reku(j,1) + cost for j in range(i+1,n) if A[j][0] - A[i][0] <= 2*T), default = inf)
            min_future_cost = min(cost_normal,cost_expection_drive)
        dp[i][exception_used] = min_future_cost
        return dp[i][exception_used]
    reku(0,0)
    return min(dp[0])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)
