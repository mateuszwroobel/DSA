def behappy(n,m,intervals):
    #f(i,p) = liczba kombinacji, aby dac dokladnie "p" prezentow pierwszym "i" dziewczynom
    # f(i,p) = sum( f(i-1, p-j) for j in range(a1,b1) if p >= j)
    dp = [[0 for _ in range(m+1)] for _ in range(n)]
    s = intervals[0][0]
    e = intervals[0][1]
    for i in range(s,e+1):
        dp[0][i] = 1
    for i in range(1,n):
        for p in range(m+1):
            start = intervals[i][0]; end = intervals[i][1]
            dp[i][p] = sum(dp[i-1][p-j] for j in range(start,end+1) if p >= j)
    return dp[n-1][m]

n = 3
m = 5
A = [[0,1],[1,3],[1,4]]

#print(behappy(n,m,A))