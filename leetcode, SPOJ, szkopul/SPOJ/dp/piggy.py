def pig_bank(E,F,n,coins):
    from math import inf
    #n - ilosc monet
    #coins[i][0] = wartosc monety
    #coins[i][1] = waga monety
    #f(i,w) - minimalna wartosc jaka mozna osiagnac
    #z pierwszych "i" monet, o dokladnej wadze "w"
    W = F - E
    dp = [[inf for _ in range(W+1)]for _ in range(n+1)]
    #base case - bierzemy 1 przedmiot
    dp[0][0] = 0
    for i in range(1,n+1):
        for w in range(W+1):
            value = coins[i-1][0]
            weight = coins[i-1][1]
            dp[i][w] = dp[i-1][w]
            if w - weight >= 0:
                dp[i][w] = min(dp[i][w-weight] + value, dp[i][w])
    return dp[n][W]

coins = [[10,3],[20,4]]
E = 1
F = 6
n = len(coins)
print(pig_bank(E,F,n,coins))


