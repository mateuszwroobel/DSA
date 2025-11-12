# LC416
def canPartition(A):
    n = len(A)
    s = sum(A)
    if s % 2 == 1:
        return False
    s = s // 2
    T = [[False for _ in range(s + 1)] for _ in range(n + 1)]
    for i in range(n):
        if A[i] > s:
            return False
    for i in range(1, n + 1):

        T[i][A[i - 1]] = True
        for j in range(1, s + 1):
            if T[i - 1][j]:
                T[i][j] = True
            elif j - A[i - 1] >= 0:
                if T[i - 1][j - A[i - 1]]:
                    T[i][j] = True
    return T[n][s]


# LC1049
def lastStoneWeightII(self, stones):
    n = len(stones)
    if n == 1:
        return stones[0]
    total = sum(stones)
    S = total // 2
    F = [[False for i in range(S + 1)] for _ in range(n)]
    F[0][0] = True
    F[0][stones[0]] = True
    for s in range(S + 1):
        for i in range(1, n):
            F[i][s] = F[i - 1][s] or F[i][s]
            if s - stones[i] >= 0:
                F[i][s] = F[i][s] or F[i - 1][s - stones[i]]
    maks = float('-inf')
    for s in range(S + 1):
        if F[n - 1][s]:
            maks = max(maks, s)
    return total - maks - maks


# lc2035 #doesnt work
def minimumDifference(A):
    n = len(A)
    total = sum(A)
    mini = min(A)
    S = sum(A) // 2
    F = [[[False, 0] for _ in range(S + 1)] for _ in range(n)]
    F[0][0] = [True, 0]
    F[0][A[0]] = [True, 1]
    for s in range(S + 1):
        for i in range(1, n):
            if F[i - 1][s][0]:
                F[i][s] = F[ i - 1][s]
            elif s - A[i] >= 0 and F[i - 1][s - A[i]][0]:
                F[i][s] = [True, F[i - 1][s - A[i]][1] + 1]
    maks = float('-inf')
    for s in range(0, S + 1):
        if F[n - 1][s][0] and F[n - 1][s][1] == n // 2:
            maks = max(maks, s)

    return (total - maks) - maks
# A = [2,-1,0,4,-2,-9]
# print(minimumDifference(A))

#LC 638
def shoppingOffers(price, special, needs):
    n = len(needs)
    m = len(special)
    #f(i,j,....n) - minimalna suma, aby kupic dokladnie "i" pierwszych itemow, "j" drugich itemow, .... n "n-tego" itemu
    #f(0,0,...,0) = base case #nie kupujemy nic
    base_case = tuple(0 for _ in range(n))
    memo = {base_case: 0}
    def rek(current):
        current = tuple(current)
        if current in memo:
            return memo[current]
        #nie uzywanie oferty
        cost = sum(current[i] * price[i] for i in range(n))
        for offer in special:
            new_needs = []
            for i in range(n):
                if current[i] < offer[i]:
                    break
                new_needs.append(current[i] - offer[i])
            #jezeli petla sie nie pezerwala oznacza ze mozemy sprobowac kupic z oferty specjalnej
            else:
                cost = min(cost, offer[-1] + rek(new_needs))

        memo[current] = cost

        return cost

    return rek(tuple(needs))







