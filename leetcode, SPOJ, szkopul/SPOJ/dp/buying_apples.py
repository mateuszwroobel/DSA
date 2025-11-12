# okreslam funkcje rekurencyjne

# f(p,w) - minimalny koszt uzywajac dokladnie "p" paczek, aby otrzymac doklkadnie "w" kilogramow jablek,
def apples(N,K,price):
    inf = float('inf')
    #K+1 - liczba kolumn (kilogramy) , N+1 - wiersze (liczba paczek)
    F = [[inf for _ in range(K+1)] for _ in range(N+1)]
    F[0][0] = 0
    #szukam najmniejszego mozliwego pakowania
    smallest = inf
    ind = None

    for i in range(len(price)):
        if price[i] != -1:
            smallest = price[i]
            ind = i
            break

    #jesli najwieksza paczka jest wieksza od "K" nie ma rozwiazania
    if ind > K:
        return -1


    for p in range(1,N+1):
        for w in range(K+1):
            for j in range(1,w+1):
                if price[j-1] != -1:
                    F[p][w] = min(F[p-1][w-j] + price[j-1], F[p][w])

    ans = min(F[p][K] for p in range(1, N+1))
    return ans if ans != inf else -1

N = 5
K = 5
price = [1,2,3,4,5]
print(apples(N,K,price))