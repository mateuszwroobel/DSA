from egz3atesty import runtests

def snow(T, I):
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
    for x,y in I:
        axis[mapped[x]] +=1
        axis[mapped[y]+1] +=-1

    curr = 0
    best = 0
    for x in axis:
        curr+=x
        best = max(curr,best)
    return best

# uruchom testy
runtests(snow, all_tests=True)