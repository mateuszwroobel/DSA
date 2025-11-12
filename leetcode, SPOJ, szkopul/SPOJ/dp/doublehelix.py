def double_helix(A,B):
    #two pointer solution
    i = 0
    j = 0
    n = len(A); m = len(B)
    sum1 = 0; sum2 = 0
    best = 0
    while i < n and j < m:
        if A[i] < B[j]:
            sum1 += A[i]
            i+=1
        elif A[i] > B[j]:
            sum2 +=B[j]
            j+=1
        else:
            #doszlismy do punktu, gdzie mozna zmienic ciag
            #wybieramy lepsza opcje i zerujemy
            best += max(sum1,sum2) + A[i]
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1
    #przepisac reszte
    while i < n:
        sum1 += A[i]
        i+=1
    while j < m:
        sum2 += B[j]
        j+=1

    return best + max(sum1,sum2)

A = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]
B = [3, 5 ,7 ,9, 20 ,25 ,30 ,40 ,55 ,56, 57, 60, 62]

print(double_helix(A,B))
