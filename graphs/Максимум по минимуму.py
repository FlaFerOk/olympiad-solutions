from collections import deque


def bfs(j):
    deq = deque()
    dist[j] = 0
    deq.append(j)
    while deq:
        ov = deq.popleft()
        for i in g[ov]:
            if dist[i] == inf:
                dist[i] = dist[ov] + 1
                deq.append(i)


n, m, s = map(int, input().split())
g = [[] for i in range(n)] 

for i in range(m):
    a, b = map(int, input().split())
    g[b - 1].append(a - 1)
    
inf = -1
dist = [inf] * n

bfs(s-1)
    
#print(dist)
print(max(dist))

