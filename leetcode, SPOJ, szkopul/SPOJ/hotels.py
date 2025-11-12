def hotels(A,M):
    n = len(A)
    best_so_far = 0
    s = 0
    left = 0
    for right in range(n):
        s += A[right]
        #przesuwamy lewy wskaznik dopoki zmniejszymy do liczby ktora mozemy osiagnac
        while s > M:
            s-=A[left]
            left+=1
        best_so_far = max(best_so_far, s)

    return best_so_far


print(hotels([2,1,3,4,5],12))