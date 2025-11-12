from email.policy import default

from egz2atesty import runtests
from math import inf


def wired(T):
    n = len(T)
    F = [[inf for _ in range(n)]for _ in range(n)]
    def wire(i,j,T):
        if i >= j: return 0
        if F[i][j] != inf: return F[i][j]
        #nielaczymy kabelkow i,j
        option2 = min((wire(i,k,T) + wire(k+1,j,T) for k in range(i+1,j,2)),
                   default=inf)
        #laczymy kabelki i,j
        option1 = abs(T[i] - T[j]) + 1  + wire(i+1,j-1,T)
        F[i][j] = min(option1,option2)
        return F[i][j]

    return wire(0,n-1,T)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wired, all_tests=True)
