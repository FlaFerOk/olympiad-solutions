n, m = map(int, input().split())
scg = [0] * (n)
for i in range(m):
    a, b = map(int, input().split())
    scg[a - 1] += 1
    scg[b - 1] += 1
print(*scg)