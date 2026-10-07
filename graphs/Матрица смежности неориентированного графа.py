n, m = map(int, input().split())

g = [[0] * n for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1][b - 1] = 1    
    g[b - 1][a - 1] = 1
    
for i in g:
    print(*i)