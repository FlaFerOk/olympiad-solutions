from collections import deque

def bfs(s, a):
    x = s[0]
    y = s[1]
    g[x][y] == a
    q = deque()
    q.append(s)
    cnt = set()
    while q:
        x, y = q.popleft()
        cnt.add((x, y))
        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < h and 0 <= ny < w:
                    if g[nx][ny] == '.':
                        g[nx][ny] = a
                        q.append([nx, ny])
                    if g[nx][ny] == '+':
                        cnt.add((nx, ny))
    return len(cnt)
                
        
h, w = map(int, input().split())
g = []
for i in range(h):
    g.append(list(input()))


for x in range(h):
    for y in range(w):
        if g[x][y] == "#":
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < h and 0 <= ny < w and g[nx][ny] == '.':
                    g[nx][ny] = "+"
                    break
                    
a = 1
ans = [1]
for x in range(h):
    for y in range(w):
        if g[x][y] == ".":
            m = bfs([x, y], a)
            ans.append(m)
            a += 1
           

print(max(ans))