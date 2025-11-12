from egz2atesty import runtests

def dominance(P):
    n = len(P)
    cnt = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x1 = P[i][0]
            y1 = P[i][1]
            x2 = P[j][0]
            y2 = P[j][1]
            if domi(x1,y1,x2,y2):
                cnt[i]+=1

    return max(cnt)

def domi(x1,y1,x2,y2):

    if x2 < x1 and y2 < y1:
        return True
    return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
