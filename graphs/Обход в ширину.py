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
        

n, s, f = map(int, input().split())
g = [list(map(int, input().split())) for i in range(n)]

inf = 10 ** 100
dist = [inf] * n

bfs(s - 1)

if dist[f - 1] == inf:
    print(0)
else:
    print(dist[f - 1])
    