#f(i) - liczba mozliwych kombinacji zajec dla przedzialow od indeksu 0 do i w posortowanej tablicy
#Sa dwie mozliwosc, albo mozna dolaczyc zajecia "i" do aktualnej kombinacji lub nie
#definuję pojecie poprzednika: poprzednik "i"-tego przedzialu to przedzial, ktory sie konczy najpozniej przed "i" oraz nie
#przecina sie z "i"
#f(i) = (f(prev) + 1) + f(i-1)
#f(prev) + 1 - aktualne zajecia i zajecie "i"
#f(i-1) - zajecia do indeksu (i-1)
#Poprzednika znajduje za pomoca sortowania po koncach przedzialu a nastepnie za pomoca binarnego wyszukiwania

def activities(intervals):
    n = len(intervals)
    intervals = sorted(intervals, key = lambda x: x[1])

    def binary_search(l,p,x):
        while l < p:
            mid = (l + p) // 2
            if intervals[x][0] >= intervals[mid][1]:
                l = mid + 1
            else:
                p = mid
        return l - 1
    prev = [binary_search(0,n-1,i) for i in range(n)]
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1,n):
        if prev[i] != -1:
            take = dp[prev[i]] + 1
        else:
            #samodzielny przedzial, ktory nie ma poprzednika zawsze mozna tak ustawic
            take = 1
        not_take = dp[i-1]
        dp[i] = take + not_take

    return dp[n-1]

intervals = [[1,3],[3,5],[5,7],[2,4],[4,6]]
print(activities(intervals))