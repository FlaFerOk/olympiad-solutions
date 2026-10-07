def printer(a):
    u = []
    for i in a:
        u.append(l[i])
    if u not in y:
        y.append(*u)
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
y = []
used = [False] * (n + 1)
per([])
print(y)
