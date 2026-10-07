def delit(n):
    d = 2
    l = [1, n]
    while d * d <= n:
        if n % d == 0:
            l.append(d)
            if n // d != d:
                l.append(n // d)
        d += 1
    l = sorted(l)
    return l


a = int(input())
y = delit(a)
print(len(y) - 2)