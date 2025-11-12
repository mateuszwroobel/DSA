#def funkcja sortujaca

def bucket_sort(T):
    n = len(T)
    buckets = [[] for i in range(n)]
    for i in range(n):
        x = int(T[i] * n)
        buckets[x].append(T[i])
    #jakas funkcja sortujaca w bucketach
    #laczenie bucketow