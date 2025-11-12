def pijemy(k, PIWO):
    n = len(PIWO)
    #Tablica do zliczania, w tablicy PIWO nie ma liczb 0, wiec wymiar wynosi k
    C = [0] * (k)
    res = []
    for i in range(n):
        C[PIWO[i]-1] += 1
    for i in range(k):
        if C[i] > 0:
            res.append(i + 1)
            C[i] -= 1
            break
    #uzupelnianie tablicy wynikowej na przemian (zakladam ze wynik zawzse istnieje_
    remaining = n-1
    i = 0
    while remaining > 0:
        for i in range(k):
            if C[i] > 0 and res[-1] != i+1:
                C[i] -= 1
                res.append(i+1)
                remaining -= 1
                break
    return res

"""
Prosimy nie modyfikować kodu poniżej :)
"""

k = int(input())
piwo = list(map(int, input().split(" ")))
n = len(piwo)
sol = [k, n] + pijemy(k, piwo)
print(" ".join(str(x) for x in sol))