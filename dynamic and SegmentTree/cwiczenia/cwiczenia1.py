def maximalRectangle(M):
    n = len(M)
    m = len(M[0])
    for i in range(n):
        for j in range(m):
            M[i][j] = int(M[i][j])
    if n == 1 and m == 1:
        return M[0][0]
    F = [[0 for _ in range(m)] for _ in range(n)]
    a = 1
    best = -1
    for j in range(m):
        F[n - 1][j] = M[n - 1][j]
        best = max(best, M[n - 1][j])
    for i in range(n):
        F[i][m - 1] = M[i][m - 1]
        best = max(best, M[i][m - 1])
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if M[i][j] == 1:
                F[i][j] = min(F[i + 1][j], F[i + 1][j + 1], F[i][j + 1]) + 1
    for i in F:
        print(i)
    return best
M = [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [0, 1, 1, 1]]

print(maximalRectangle(M))