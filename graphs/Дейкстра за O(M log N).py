from collections import deque


def dijkstra(s, d):
    d[s] = 0
    q = []
    q.append([d[s], s])
    while q:
        q.sort(reverse=True)
        t = q.pop()
        for v in range(n):
            if d[v] > d[t[1]] + g[t[1]][v]:
                d[v] = d[t[1]] + g[t[1]][v]
                q.append([d[v], v])
    
    

n, m, s = map(int, input().split())

g = []
inf = 10 ** 10

for _ in range(n):
    g.append([inf] * n)

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c
    g[b][a] = c

dist = [inf] * n

dijkstra(s, dist)

print(*dist)
