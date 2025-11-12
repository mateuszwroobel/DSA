from egzP4atesty import runtests 
#zadanie mozna potraktowac jako szukanie najdluzszego rosnacego podciagu
#nalezy posortowac po pierwsze wspolrzednej, a gdy sa takie same to malejaco po drugiej
#Nasza odpowiedzia bedzie wtedy dlugosc najdluzszego rosnacego podciagu po drugiej wspolrzednej
#Co nam daje sortowanie:
#rozwazmy nastepujace pary
#2-8
#2-6
#2-5
#Gdy mam posortowane w taki sposob, pary o takiej samej pierwszej liczbie jak rozpatrywana napewno
#nie beda tworzyc mi podciagu. Gdybym mial posortowane w taki sposob:
#2-5,2-6,2-8 to wykryje mi podciag rosnacy poniewaz chce sprawdzac tylko jedna wspolrzedna (druga)
#Aby zoptymalizowac do O(nlogn) uzywam algorytmu LIS wykorzystujacego binarne wyszukiwanie


def mosty (T):
    n = len(T)
    T = sorted(T, key=lambda x: (x[0],-x[1]))
    A = [y for x,y in T]

    def binary_search(arr, l, p , x):
        while l < p:
            mid = (l+p)//2
            if arr[mid] <= x:
                l = mid + 1
            else:
                p = mid
        return l

    lis = [A[0]]
    for i in range(1,n):
        k = len(lis)
        last = lis[-1]
        if A[i] > last:
            lis.append(A[i])
        else:
            index = binary_search(lis,0,k,A[i])
            lis[index] = A[i]

    return len(lis)
runtests ( mosty, all_tests=True )