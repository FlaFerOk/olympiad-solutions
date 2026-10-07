def printer(a):
    for i in a:
        print(l[i], end="")
    print()
    return


def per(s):
    if len(s) == n:
        printer(s)
        return
    for i in range(n):
        if used[i]:
            continue
        used[i] = True
        per(s + [i])
        used[i] = False


l = input()
n = len(l)
used = [False] * (n + 1)
per([])