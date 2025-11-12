from egz3btesty import runtests


def kunlucky(T, k):
    n = len(T)
    unlucky = {}
    i = 1
    while k < n:
        unlucky[k] = True
        k =  k + (k%i) + 7
        i+=1

    #two pointers solution
    i = 0
    curr = 0
    best = 0
    for j in range(n):
        #przesuwaj prawy indeks
        if T[j] in unlucky:
            curr+=1
        #przesuwaj lewy indeks, jesli masz za duzo pechowych
        while curr > 2:
            if T[i] in unlucky:
                curr -= 1
            i+=1
        best = max(best,j-i+1)


    return best


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kunlucky, all_tests=True)
