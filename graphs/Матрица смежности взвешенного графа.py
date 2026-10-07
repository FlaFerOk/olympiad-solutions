n = int(input())

g = []
mn = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
mx = 0

for i in range(n):
    g.append(list(map(int, input().split())))
    for j in g[i]:
        if j != 0:
            mn = min(mn, j)
    mx = max(mx, max(g[i]))

lmx = []
lmn = []

for i in range(n):
    for j in range(i + 1, n):
        if g[i][j] == mx:
            lmx.append([i+1, j+1])
        elif g[i][j] == mn:
            lmn.append([i+1, j+1])

for i in lmx:
    print(*i)
for i in lmn[::-1]:
    print(*i)
