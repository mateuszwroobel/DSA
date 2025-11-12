from egz3atesty import runtests
#(O T*N)
def snow(T, I):
    max_point = max(stop for start, stop in I)
    axis = [0] * (max_point + 1)

    for start, stop in I:
        for i in range(start, stop + 1):
            axis[i] += 1

    return max(axis)

# uruchom testy
runtests(snow, all_tests=True)
