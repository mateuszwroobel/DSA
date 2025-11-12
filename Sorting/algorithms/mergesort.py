
def number(A,B,diff):
    counter = 0
    n = len(A)
    C = [A[i] - B[i] for i in range(n)]
    def mergesort(A, l, p):
        if l == p:
            return A[l]
        mid = (l + p) // 2
        mergesort(A, l, mid)
        mergesort(A, mid + 1, p)
        merge(A, l, mid, p)

    def merge(A, l, mid, p):
        i = j = 0
        k = l
        left = A[l:mid + 1]
        right = A[mid + 1:p + 1]
        nl = len(left)
        nr = len(right)
        nonlocal diff
        nonlocal counter


        while i < nl and j < nr:
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < nl:
            A[k] = left[i]
            i += 1
            k += 1
        while j < nr:
            A[k] = right[j]
            j += 1
            k += 1
    mergesort(C, 0, n - 1)
    return counter


print(number([3,2,5],[2,2,1],1))

