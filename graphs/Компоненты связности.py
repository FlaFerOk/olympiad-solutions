def dfs(o):
    used[o] = 1
    for i in range(n):
        if g[o][i] == 1 and used[i] == 0:
            dfs(i)

n = int(input())

g = []

for i in range(n):
    g.append(list(map(int, input().split())))
    
used = [0] * n
ks = 0

for s in range(n):
    if used[s] == 0:
        dfs(s)
        ks += 1
        
print(ks)
