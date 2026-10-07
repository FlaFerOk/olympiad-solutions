n = int(input())
a = list(map(int, input().split()))

l = [0] * (n + 1)
for i in a:
    l[i] += 1
d = 0
max_cl = l.index(max(l))
for i in range(n):
    if a[i] != max_cl:
        a[i] = max_cl
        if i + 1 <= n - 1:
            a[i + 1] = max_cl
        d += 1

print(d)
