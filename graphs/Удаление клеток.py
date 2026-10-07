from collections import deque

def bfs(x, y):
    g[x][y] = '@'
    q = deque()
    q.append(x)
    q.append(y)
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    while q:
        x = q.popleft()
        y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < n and 0 <= Y < m and g[X][Y] == '#':
                g[X][Y] = '@'
                q.append(X)
                q.append(Y)


n, m = map(int, input().split())
g = [list(input()) for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '#':
            cnt += 1
            bfs(i, j)
print(cnt)