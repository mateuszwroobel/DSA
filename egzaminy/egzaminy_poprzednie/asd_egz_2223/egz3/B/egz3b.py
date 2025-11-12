from egz3btesty import runtests
#przedzialy ktore sie przecinaja musza byc obok siebie w posortowanej tablicy po drugiej
#Rozwazmy sytuacje przeciwna:
#Uznajmy ze sa przedzialy, ktore sie przecinaja ale nie leza obok siebie w tablicy
#
def uncool(P):
    n = len(P)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            start1 = P[i][0]
            end1 = P[i][1]
            end = P[j][1]
            start = P[j][0]
            if not_fine(start,end,start1,end1):
                return i,j
    return
def not_fine(start,end,start1,end1):
    if start < start1 < end < end1: return True
    else: return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(uncool, all_tests=True)
