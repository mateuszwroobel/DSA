def bat1(ratings, batches, weapons, k):
    #k - money Wayne can spend on weapons
    #f(i,c) - max liczba mocy, ktora mozna
    #uzyskac z pierwszych "i" "batches", nie przekraczajaca c
    #batches - tablica z kosztem otwarcia batcha
    #weapon - macierz z kosztem broni w "i"-tym batchu
    #ratings- macierz z ratingiem
    #"k" - pieniadze ktore mozna wydac

    n = len(batches)
    m = len(weapons[0])
    dp = [[[0 for _ in range(n)] for _ in range(m)]for _ in range(k+1)]

    #base case: szukam pierwszego przedmiotu ktory moge kupic


# k = 20
# batches = [3 ,4]
# weapons = [[3, 2, 3 ,2],
#     [3,2,3,5]]
# ratings = [[3,2,3,2],
# [4, 5, 6, 5,]]


def bat2(A):
    #lis
    #f(i) - najdluzszy rosnacy podciag gdyby konczyl sie na "i"
    n = len(A)
    def lis(A):
        n = len(A)
        dp = [1] * n
        prev_index = [-1] * n

        for i in range(1,n):
            for j in range(i):
                if A[j] < A[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j

        return dp

    return


A = [5,3,4,6,1,2]
print(bat2(A))

