def JobScheduling(jobs):
    n = len(jobs)
    N = 0
    for i, d, p in jobs:
        N = max(d, N)
    dl = [-1 for _ in range(N)]
    print(dl)
    jobs = sorted(jobs, key=lambda x: -x[2])
    print(jobs)
    profit = 0
    c = 0
    for i, d, p in jobs:
        print(dl)
        if dl[d-1] == -1:
            dl[d-1] = p
            profit += p
            c += 1
        else:
            for j in range(d - 2, 1):
                if dl[j] == -1:
                    dl[j] = p
                    profit += p
                    c += 1
                    break
    print(profit,c)

Jobs = [ [1, 2, 100] , [2, 1, 19] , [3, 2, 27] , [4, 1, 25] , [5, 1, 15] ]
JobScheduling(Jobs)