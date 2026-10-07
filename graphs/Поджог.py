from collections import deque


def bfs(j):
    deq = deque()
    for i in j:
        dist[i-1] = 0
        deq.append(i-1)
    while deq:
        ov = deq.popleft()
        for i in g[ov]:
            if dist[i] == inf:
                dist[i] = dist[ov] + 1
                deq.append(i)


n, m = map(int, input().split())
g = [[] for i in range(n)] 

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
    
inf = 10 ** 9
input()
dist = [inf] * n

s = list(map(int, input().split()))
bfs(s)
    
#print(dist)
md = max(dist)
print(md)
otv = []
for i in range(n):
    if dist[i] == md:
        otv.append(i)
print(min(otv)+1)