def dfs(v):
    global f
    used[v] = 1
    for u in range(n):
        if g[v][u] == 1:
            if used[u] == 0:
                dfs(u)
            elif used [u] == 1:
                f = True
    used[v] = 2
    

n = int(input())
g = [list(map(int, input().split())) for i in range(n)]

used = [0] * n
f = False

for i in range(n):
    if f == False and used[i] == 0:
        dfs(i)
        
print(int(f))