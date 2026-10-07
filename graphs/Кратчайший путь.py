from collections import deque

def bfs(v):
    deq = deque()
    dist[v] = 0
    deq.append(v)
    while deq:
        ov = deq.popleft()
        for i in g[ov]:
            if dist[i] == inf:
                dist[i] = dist[ov] + 1
                frm[i] = ov
                deq.append(i)
                

n, m = map(int, input().split())
a, b = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    v1, v2 = map(int, input().split())
    g[v1 - 1].append(v2 - 1)
    g[v2 - 1].append(v1 - 1)

inf = -1
frm = [-1] * n
dist = [inf] * n
ans = []

bfs(a - 1)

ans.append(b-1)
print(dist[b - 1])
while frm[ans[-1]] != -1:
    ans.append(frm[ans[-1]])
    
for i in ans[::-1]:
    print(i + 1, end=" ")
    
    
    
    
    
    
    
    
    
    
    
    