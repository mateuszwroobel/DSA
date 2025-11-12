from math import inf

# f(k,i,b,c) - max benefit w "k-tym" dniu, gotujac maksymalnie
# "i" pierwszych dan nie przekraczajac budzetu calkowitego "b" gotujac danie po raz "c"
# ODP: f(K-1,N-1,B,1) lub f(K-1,N-1,B,0)
# f(k,i,b) sa dwie mozliwosci
# 1 - nie gotuje "i-tego" dania: f(k,i-1,b,c)
# 2 - gotuje "i" te danie:
# Gotujac "i-te" danie tez mamy dwie mozliwosci
# Gotujemy to samo co poprzednio albo inne
#Inne: f(k,i-1,b-cost[i],c) + benefit[i]
#To samo: f(k,i,b-cost[i],c-1) + benefit[i] * 0,5

#wartosci "c" - 0: gotowalem raz
#1 - gotowalem drugie raz
def menu(K,N,M,benefit,cost):
    dp = [[[[0 for _ in range(3)] for _ in range(M+1)]\
        for _ in range(N)] for _ in range(K)]

    #Gotuje pierwsze danie w pierwszym dniu po raz pierwszy
    for i in range(N):
        for b in range(cost[0],M+1):
            dp[0][i][b][1] = benefit[0]

    for k in range(K):
        for i in range(1,N):
            for b in range(M+1):
                for c in range(1,3):
                    cook_another = -inf
                    cook_again = -inf
                    not_cook = dp[k][i-1][b][c]
                    if b >= cost[i]:
                        cook_another = dp[k][i-1][b-cost[i]][c] + benefit[i]
                        cook_again = dp[k][i][b-cost[i]][c-1] + benefit[i] * (0.5)
                    dp[k][i][b][c] = max(not_cook, cook_another, cook_again)


    return max(dp[K-1][N-1][M])

