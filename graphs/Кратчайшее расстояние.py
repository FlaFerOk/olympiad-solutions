from collections import deque
def bfs(v):
    dist[v] = 0
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        for u in range(n):
            if g[cur][u] == 1 and dist[u] == inf:
                dist[u] = dist[cur] + 1
                q.append(u)
        

n, x = map(int, input().split())
g = [list(map(int, input().split())) for i in range(n)]

inf = -1
dist = [inf] * n

bfs(x - 1)

print(*dist)