from egz1btesty import runtests
from math import inf
def planets( D, C, T, E ):
    n = len(D)
    F = [[inf for _ in range(E+1)] for _ in range(n)]
    F[0][0] = 0
    for i in range(1,E+1):
        F[0][i] = F[0][i-1] + C[0]
    for i in range(1,n):
        dist = D[i] - D[i-1]
        for b in range(E+1):
            if b == 0:
                for t in range(i): #to - teleport to
                    if T[t][0] == i:
                        cost = T[t][1]
                        F[i][b] = min(F[t][b] + cost, F[i][b]) #uzywanie teleportow
                #nie uzywanie teleportu (sytuacja tez gdy go nie ma)
                F[i][b] = min(F[i][b], F[i-1][b+dist])
            else:
                F[i][b] = F[i][b-1] + C[i] #tankowanie na stacji i
                if b + dist <= E:
                    F[i][b] = min(F[i-1][b + dist], F[i][b])
    return F[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
