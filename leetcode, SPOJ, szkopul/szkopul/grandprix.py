from math import inf
def grand_prix(D,C,k,s):
    D.append(s)
    C.append(0)
    n = len(D) + 1
    #dodaje stacje 0 i s do tablic
    T = [0 for _ in range(n)]
    c = [0 for _ in range(n)]
    for i in range(n-1):
        c[i+1] = C[i]
        T[i+1] = D[i]
    #f(i,b) - minimalny koszt bedac w stacji o indeksie "i" majac "b" paliwa
    F = [[inf for _ in range(k+1)] for _ in range(n)]

    #base case - pierwsza stacja darmowa
    for i in range(k+1):
        F[0][i] = 0
    for i in range(1,n):
        for b in range(k+1):
            #odleglosc miedzy miastami
            d = T[i] - T[i-1]
            if b == 0:
                for j in range(1,4):
                    #uzywanie napedu
                    if i >= j:
                        F[i][b] = min(F[i][b],F[i-j][k])
                if b + d <=k:
                    F[i][b] = min(F[i][b],F[i-1][b+d]) #nie uzywanie napedu
            else:
                F[i][b] = F[i][b-1] + c[i] #ladowanie na stacji "i"
                if b + d <= k:
                    F[i][b] = min(F[i][b],F[i-1][b+d])
    return F[n-1][0]


D = [2, 6, 8, 9, 11, 12]; C = [5, 3, 1, 4, 2, 9]; k = 5; s = 15

print(grand_prix(D,C,k,s))