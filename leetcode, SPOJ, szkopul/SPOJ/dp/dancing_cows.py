def dcows(bulls,cows):
    #f(i,j) - minimalna wartosc zakladajac ze lacze byka o indeksie "i"  z krowa o indeksie "j"
    bulls.sort()
    cows.sort()
    n = len(bulls)
    m = len(cows)
    dp = [[float("inf") for _ in range(m)] for _ in range(n)]

    for cow in range(m):
        dp[0][cow] = abs(bulls[0] - cows[cow])
    for i in range(1,n):
        best_previous = float('inf')
        for j in range(m):
            connect = best_previous + abs(bulls[i] - cows[j])
            dp[i][j] = min(connect, dp[i][j])
            best_previous= min(dp[i-1][j], best_previous)


    return min(dp[n-1])

bulls = [10, 10, 12, 13, 16]
cows =  [6 ,7, 9, 10, 11, 12, 17]
print(dcows(bulls,cows))