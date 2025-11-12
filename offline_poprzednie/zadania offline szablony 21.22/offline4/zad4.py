from zad4testy import runtests

def select_buildings(T,p):
    n = len(T)
    T_ind = [T[i] + (i,) for i in range(n)]
    T= sorted(T_ind,key = lambda x: x[2])
    F =[[0 for _ in range(p+1)] for _ in range(n)]
    decisions = [[None for _ in range(p + 1)] for _ in range(n)]
    cap = [h*(b-a) for h,a,b,w, _ in T]

    cost = [w for h,a,b,w,_ in T]

    for P in range(cost[0],p + 1):
        F[0][P] = cap[0]
        decisions[0][P] = (None,P)

    prev = [None for _ in range(n)]
    for i in range(n):
        prev[i] = prev1(T,i)

    for i in range(1,n):
        for j in range(p+1):
            F[i][j]= F[i-1][j]
            decisions[i][j] = (i-1,j)
            if j >= cost[i]:
                if F[i][j]  < cap[i]: #samodzielny budynek
                    F[i][j] = cap[i]
                    decisions[i][j] = (None,j)
                if j - cost[i] >= 0 and prev[i] != - 1:
                     if F[i][j] < F[prev[i]][j-cost[i]] + cap[i]:
                        F[i][j]= F[prev[i]][j - cost[i]] + cap[i] #buduje
                        decisions[i][j] = (prev[i],j-cost[i])

    res = []
    budget = p
    curr_i = n-1

    while curr_i is not None:
        prev_i, prev_j = decisions[curr_i][budget]
        if prev_i is None:
            res.append(T[curr_i][4])
        elif F[curr_i][budget] != F[prev_i][prev_j]:
            res.append(T[curr_i][4])
        curr_i, budget = prev_i, prev_j
    return res

def prev1(T,i):
    start = T[i][1]
    for j in range(i-1,-1,-1):
        if T[j][2] < start :
            return j
    return -1



runtests( select_buildings )