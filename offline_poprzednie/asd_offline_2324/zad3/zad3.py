from zad3testy import runtests

def dominance(P):
  n = len(P)
  Tx = [0 for i in range(n+1)]
  Ty = [0 for i in range(n+1)]
  for i in range(n):
    Tx[P[i][0]] += 1
    Ty[P[i][1]] += 1
  for i in range(n-1,-1,-1):
    Tx[i] += Tx[i+1]
    Ty[i] += Ty[i+1]
  min1 = Tx[P[0][0]] + Ty[P[0][1]]
  for i in range(1,n):
    x = P[i]
    new_sum = Tx[x[0]]+ Ty[x[1]]
    min1 = min(new_sum,min1)
  return n - min1 + 1


# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( dominance, all_tests = True )
