def factor(a):
    l = []
    i = 2
    while i * i <= a:
        while a % i == 0:
            l.append(i)
            a //= i
        i+=1
    if a != 1:
        l.append(a)
    return l


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


x, b = map(int, input().split())
f = factor(x)
#print(f)
if f[-1] > b:
    print(-1)
else:
    ans = []
    delit_ = delit(x)
    for i in delit_[:0:-1]:
        if x % i == 0 and i <= b:
            ans.append(i)
            x //= i
    print(len(ans))
    print(*ans)