n, m, l, r = map(int, input().split())

if l == r:
    q = m-1
else:
    q = m

a = []
for i in range(1, n + 1):
    if l <= i <= r:
        a.append(m)
    else:
        if i < l:
            if l - i == 2:
                a.append(m-1)
            elif (l - i) % 2 == 0:
                a.append(q)
            else:
                a.append(-m)
        else:
            if i - r == 2:
                a.append(m-1)
            elif (i - r) % 2 == 0:
                a.append(q)
            else:
                a.append(-m)

print(*a)
