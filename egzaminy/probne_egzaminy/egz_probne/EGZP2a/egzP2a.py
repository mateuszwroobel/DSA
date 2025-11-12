from egzP2atesty import runtests

def zdjecie(T, m, k):
    n = len(T)
    start = [0 for _ in range(m)] #poczatkowe indeksy
    end = [0 for _ in range(m)] #koncowe
    start[0] = 0        #ostatni indeks w 0 rzedzie (od gory), gdyby numerowac po kolei od 0 po rzedach
    end[0] = k + m - 2  #ostatni indeks w 0 rzedzie (od gory), gdyby numerowac po kolei od 0 po rzedach
    for i in range(1,m):
        start[i] = end[i-1] + 1
        end[i] = start[i] + k + m - 2 - i
    ind = [0 for _ in range(n)] #tablica do zamiany indeksow
    for i in range(n):
        row = i % m
        col = i // m
        ind[i] = start[row] + col

    def partition(A, p, r,ind):
        n = len(A)
        x = A[ind[r]][1]
        i = p - 1
        for j in range(p, r):
            if A[ind[j]][1] >= x:
                i += 1
                A[ind[i]], A[ind[j]] = A[ind[j]], A[ind[i]]
        A[ind[r]], A[ind[i + 1]] = A[ind[i + 1]], A[ind[r]]
        return i + 1


    def quicksort(A, p, r,ind):
        if p < r:
            q = partition(A, p, r,ind)
            quicksort(A, p, q - 1,ind)
            quicksort(A, q + 1, r,ind)

    quicksort(T,0,len(T)-1,ind)
    return None


runtests (zdjecie, all_tests=False)