def wyprawy(WI):
    n = len(WI)
    A = sorted(WI, key=lambda x: x[1])
    F = [0 for _ in range(n)]
    F[0] = A[0][2]

    # indeks ktory sie nie przecina i konczy najpozniej
    prev = [None for _ in range(n)]
    ends  = [e for s,e,c in A]
    for i in range(n):
        prev[i] = bi_search(ends,0,i,A[i][0])

    # dla indeksu i mam nastepujacy wybor:
    # zabieram wartosc wiadra jesli juz wrocilem
    # nie zabieram
    for i in range(1, n):
        # nie zabieram wiadra
        F[i] = F[i - 1]
        if prev[i] is None:
            # moze oplaca sie wziasc jedynie wiadro
            F[i] = max(F[i - 1], A[i][2])
        # moge zabrac
        else:
            F[i] = max(F[i], F[prev[i]] + A[i][2]) 
    return F[n - 1]

def bi_search(e,l,p,s):
    #upper bound
    while l < p:
        mid = (l + p) // 2
        if e[mid] <= s:
            l = mid + 1
        else:
            p = mid
    return l-1 if l > 0 else None

"""
Uprzejmie prosimy o niemodyfikowanie poniższego kodu :)
"""

line = input()
data = list(map(int, line.strip().split()))
n = len(data) // 3
WI = [None] * n
for i in range(n):
    WI[i] = (data[i * 3], data[i * 3 + 1], data[i * 3 + 2])
print(wyprawy(WI))
