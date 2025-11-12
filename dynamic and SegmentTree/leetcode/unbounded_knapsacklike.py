# lc 322
c = [1, 2, 5]
Target = 11

def coin_change(coins, T):
    F = [float('inf') for _ in range(T + 1)]
    F[0] = 0
    n = len(coins)
    for coin in coins:
        for t in range(1, T + 1):
            F[t] = min(F[t],F[t-coin]+1)
    return F[T]


def numSquares(n):
    numbers = [a for a in range(n+1)]
    coins = []
    for x in numbers:
        if x**2 <= n:
            coins.append(x*x)
    print(coins)
    F = [float('inf') for _ in range(n + 1)]
    F[0] = 0
    for coin in coins:
        for t in range(1, n + 1):
            if t - coin >= 0:
                F[t] = min(F[t],F[t-coin]+1)
    return F[n]



def min_cost(cost):
    n = len(cost)
    inf = float('inf')
    F = [[inf for _ in range(3)] for _ in range(n)]
    F[0][0] = cost[0][0]
    F[0][1] = cost[0][1]
    F[0][2] = cost[0][2]
    for i in range(1,n):
        best = inf
        for j in range(3):
            if j == 0:
                best = min(F[i-1][1],F[i-1][2])
            if j == 1:
                best = min(F[i-1][0],F[i-1][2])
            if j == 2:
                best = min(F[i-1][0],F[i-1][1])
            F[i][j] = cost[i][j] + best
    return min(F[n-1])

cost = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]



def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    F = [0 for i in range(n)]
    F[0] = nums[0]
    F[1] = max(F[0], nums[1])
    for i in range(2, n):
        F[i] = max(F[i - 2] + nums[i], F[i - 1])
    return F[n - 1]



def bricks(A):
    n = len(A)
    F = [1] * n
    for i in range(1,n):
        for j in range(i):
            if A[j][0] <= A[i][0] and A[j][1] >= A[i][1]:
                F[i] = max(F[i],F[j]+1)
    return n - max(F)

ranges = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]

print(bricks(ranges))