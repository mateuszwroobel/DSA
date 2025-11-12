from networkx.algorithms.regular import k_factor

from egz2btesty import runtests

#f(i) - maksymalny liczba sztabek zlota bedac w komnacie o indeksie i

def magic(C):
    n = len(C)
    visited = [False] * n
    visited[0] = True
    dp = [-1] * n
    dp[0]= 0

    for i in range(n):
        if dp[i] == -1:
            continue
        #Jesli komnata jest nieosiagalna - pomin
        for k in range(1,4):
            gold_in_room = C[i][0]
            next_room = C[i][k][1]
            gold_to_open = C[i][k][0]

            if next_room == -1 or next_room < i:
                continue

            #Okazuje sie ze trezba brac cale zloto z komanty ale w tresci tego nie ma
            if gold_in_room - gold_to_open <= 10:
                potential_profit = gold_in_room - gold_to_open
                dp[next_room] = max(potential_profit + dp[i], dp[next_room])

    return dp[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True)