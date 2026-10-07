from collections import deque

def bfs(x, y):
    g[x][y] = [x, y]
    q = deque()
    q.append(x)
    q.append(y)
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, 2, -2, 2, -2, 1, -1]
    while q:
        x = q.popleft()
        y = q.popleft()
        for i in range(8):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < 8 and 0 <= Y < 8 and g[X][Y] == inf:
                g[X][Y] = [x, y]
                q.append(X)
                q.append(Y)


inf = 10 ** 10
g = [[inf] * 8 for i in range(8)]
a = list(input())
b = list(input())
a[1] = int(a[1]) - 1 
b[1] = int(b[1]) - 1
a[0] = ord(a[0]) - 97
b[0] = ord(b[0]) - 97
bfs(a[0], a[1])
ans = []
ans.append(b)

while ans[-1] != a:
    ans.append(g[ans[-1][0]][ans[-1][1]])
  
for i in ans[::-1]:
    print(chr(i[0]+97), i[1] + 1, sep="")