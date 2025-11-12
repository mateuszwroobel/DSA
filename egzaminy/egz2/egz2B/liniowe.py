from egz2Btesty import runtests


def bitgame(T):
    stack = []
    for x in T:
        collision = False
        while stack and stack[-1] <= x:
            stack.pop()
            collision = True
        if not collision:
            stack.append(x)

    return len(stack)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(bitgame, all_tests=True)
