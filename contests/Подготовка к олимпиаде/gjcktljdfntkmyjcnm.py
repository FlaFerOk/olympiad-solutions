def el(a):
    i = 1
    k = 10
    if a < 10:
        return a
    while 1:
        if a - (k + 10 * i) < 0:
            return (a - k) // i
        i += 1
        k += 10 * i


n, m = map(int, input().split())
for i in range(n - 1, m):
    print(el(i))