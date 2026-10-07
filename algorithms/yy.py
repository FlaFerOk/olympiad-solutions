def er(m, n):
    p = [1] * (n + 1)
    p[0] = 0
    p[1] = 0
    pp = []
    for i in range(n + 1):
        if p[i] == 1:
            if m <= i <=n:
                pp.append(i)
            for j in range(i * i, n + 1, i):
                p[j] = 0
    return pp


k = int(input())
mn = list()
mi = 0
ma = 0
for i in range(k):
    m, n = map(int, input().split())
    mn.append([m, n])
    if n > ma:
        ma = n
    if m < mi:
        mi = m
a = er(mi, ma)
for i in a:
    