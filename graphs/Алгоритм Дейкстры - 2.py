from collections import deque


def dijkstra(s, d):
    d[s] = 0
    q = []
    frm[s] = s
    q.append([d[s], s])
    while q:
        q.sort(reverse=True)
        t = q.pop()
        for v in range(n):
            if d[v] > d[t[1]] + g[t[1]][v]:
                d[v] = d[t[1]] + g[t[1]][v]
                frm[v] = t[1]
                q.append([d[v], v])
    
    

n, s, f = map(int, input().split())

g = []

for _ in range(n):
    g.append(list(map(int, input().split())))
    
inf = 10 ** 10

for i in range(n):
    for j in range(n):
        if g[i][j] == -1:
            g[i][j] = inf

frm = []
for _ in range(n):
    frm.append([-1] * n)
dist = [inf] * n

dijkstra(s-1, dist)

print(*dist)

if frm[f] == -1:
    print(-1)
else:
    ans = []
    ans.append(f)
    while ans[-1] != s:
        ans.append(frm[ans[-1]])
        print(ans)

    print(ans[:-1:-1])
    
    
    