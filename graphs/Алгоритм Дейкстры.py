from collections import deque


def dijkstra(s, d):
    d[s] = 0
    q = []
    q.append([d[s], s])
    while q:
        q.sort(reverse=True)
        t = q.pop()
        for v in range(m-1):
            if d[v] > d[t[1]] + g[t[1]][v]:
                d[v] = d[t[1]] + g[t[1]][v]
                q.append([d[v], v])
    
    

n, s, f = map(int, input().split())

g = []

for _ in range(m):
    g.append(list(map(int, input().split())))
    
inf = 10 ** 10

for i in range(n):
    for j in range(n):
        if g[i][j] == -1:
            g[i][j] = inf

dist = [inf] * n

dijkstra(s-1, dist)

print(*dist)