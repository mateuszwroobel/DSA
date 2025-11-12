from kol1testy import runtests


# ide od konca i rozpatruje tylko elementy wieksze od dotychczas napotkanej wiekszej wartosci,
# bo tylko one moga dac wieksza "rangę"
#O(n^2)

def maxrank(T):
    n = len(T)
    maxi = 0
    best = 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        #rozpatruje jesli jest wiekszy niz dotychczasowe maximum
        if T[i] > maxi:
            maxi = T[i]
            cnt = 0
            for j in range(i,-1,-1):
                if T[j] < T[i]:
                    cnt+=1
            best = max(best,cnt)

    return best


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxrank, all_tests=True)
