from collections import deque

def bfs(x, y):
    g[x][y] = "@"
    size = 1
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
            if 0 <= X < n and 0 <= Y < n and g[X][Y] == '.':
                g[X][Y] = "@"
                size += 1
                q.append(X)
                q.append(Y)
    return size


n = int(input())
g = [list(input()) for i in range(n)]
a1, a2 = map(int, input().split())
print(bfs(a1 - 1, a2 - 1))
