from kolutesty import runtests


def ice_cream(T):
    T.sort(reverse=True)
    time = 0
    s = 0
    for v in T:
        if v - time >= 0:
            s += v - time
        else:
            return s
        time += 1
    return s


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ice_cream, all_tests=True)
