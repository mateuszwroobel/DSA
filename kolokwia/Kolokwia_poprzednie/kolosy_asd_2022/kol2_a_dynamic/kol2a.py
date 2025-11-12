from email.policy import default

from kol2atesty import runtests
from math import inf


from email.policy import default

from kol2atesty import runtests
from math import inf


def drivers(P, B):
    n = len(P)
    A = [None for _ in range(n + 1)]
    A[0] = (0, True)
    for i in range(n):
        A[i + 1] = (P[i][0], P[i][1])
    A.sort()
    dist = [None for _ in range(n + 1)]
    control = 0
    for i, (x, is_transfer) in enumerate(A):
        if not is_transfer:
            control += 1
        if is_transfer:
            dist[i] = (x, is_transfer, control)
            control = 0
    F = [[[inf for _ in range(2)] for _ in range(3)] for _ in range(n + 1)]
    changes = []
    def reku(i, k, driver):
        if A[i] is None: return 0
        if i == n + 1 or k == 3: return 0
        if F[i][k][driver] != inf: return F[i][k][driver]
        controls = 0
        for u in range(i+1,n+1):
            if dist[u] is not None:
                controls = dist[u][2]
                break
        if driver == 0:
            # Jedzie marian i bedzie jechal dalej
            option1 = min((reku(j, k + 1, driver)  for j in range(i + 1, n+1)),default = inf)

            # Jedzie marian i sie przesiadzie
            option2 =   min((reku(j, 0, 1)  for j in range(i + 1, n+1)),default = inf)
            F[i][k][driver] = min(option1,option2) + controls
        else:
            #Jedzie jacek i bedzie jechal dalej, gdy jedzie jacek nie liczymy pkt controlnych
            option1 = min((reku(j,k+1,driver) for j in range(i+1,n+1)),default = inf)
            #Jedzie jacek i sie przesiada
            option2 = min((reku(j,k,0) for j in range(i+1,n+1)), default = inf)
            F[i][k][driver] = min(option1,option2)
        return F[i][k][driver]

    print(reku(0,0,1))
    return changes

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(drivers, all_tests=False)
