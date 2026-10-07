def er(n):
    p = [1] * (n + 1)
    p[0] = 0
    p[1] = 0
    pp = []
    for i in range(n + 1):
        if p[i] == 1:
            pp.append(i)
            for j in range(i * i, n + 1, i):
                p[j] = 0
    return pp


def true_gip(a):
    pp = er(a)
    for i in pp:
        if a - i in pp:
            return i, a - i


n = int(input())
print(*true_gip(n))