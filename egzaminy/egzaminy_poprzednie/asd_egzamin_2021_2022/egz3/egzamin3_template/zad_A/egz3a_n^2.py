from egz3atesty import runtests

def snow( T, I ):
    #compress points
    cord = []
    used = {}
    for start,stop in I:
        if start not in used:
            cord.append(start)
            used[start] = True
        if stop not in used:
            cord.append(stop)
            used[stop] = True
    cord.sort()
    mapped = {x: i for i,x in enumerate(cord)}
    n = len(I)
    axis = [0] * (2*n+1)
    for start,stop in I: #O(n)
        a = mapped[start]
        b = mapped[stop]
        for i in range(a,b+1): #O(2n)
            axis[i]+=1

    return max(axis)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )