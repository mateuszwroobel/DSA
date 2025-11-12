def pijemy(k, PIWO):
    n = len(PIWO)
    #Tablica do zliczania, w tablicy PIWO nie ma liczb 0, wiec wymiar wynosi k
    C = [0] * (k)
    res = []
    for i in range(n):
        C[PIWO[i]-1] += 1
    res.append(1)
    C[0] = C[0] - 1
    #uzupelnianie tablicy wynikowej na przemian (zakladam ze wynik zawzse istnieje_
    remaining = n-1
    i = 0
    while remaining > 0:
        if C[i] > 0 and res[-1] != i+1:
            C[i] -= 1
            res.append(i+1)
            remaining -= 1
        i += 1
        if i == k:
            i = 0
    return res

print(pijemy(3,[1,2,2,1,3,1,1,1,2,1,2,2,3,3,3]))