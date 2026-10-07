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
        

n = int(input())
g = [list(map(int, input().split())) for i in range(n)]
x, y = map(int, input().split())

inf = -1
dist = [inf] * n

bfs(x - 1)

print(dist[y-1])