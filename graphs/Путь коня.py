from collections import deque

def bfs(x, y):
    frm[x][y] = [x, y]
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
            if 0 <= X < n and 0 <= Y < n and (g[X][Y] == "." or g[X][Y] == "@") and frm[X][Y] == -1:
                frm[X][Y] = [x, y]
                q.append(X)
                q.append(Y)


n = int(input())
g = []

for _ in range(n):
    g.append(list(input()))

frm = [[-1] * n for i in range(n)]
ab = []
for i in range(n):
    for j in range(n):
        if g[i][j] == "@":
            ab.append([i, j])    

bfs(ab[0][0], ab[0][1])

if frm[ab[1][0]][ab[1][1]] == -1:
    print("Impossible")
else:
    ans = []
    ans.append([ab[1][0], ab[1][1]])
    while ans[-1] != ab[0]:
        g[ans[-1][0]][ans[-1][1]] = "@"
        ans.append(frm[ans[-1][0]][ans[-1][1]])
        
    for i in g:
        print(*i, sep="")
    
            