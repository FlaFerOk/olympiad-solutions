def dfs(o):
    used[o] = 1
    print(o+1, end=" ")
    for i in g[o]:
        if used[i] == 0:
            used[i] = 1
            dfs(i)

n, m = map(int, input().split())

g = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    
v = int(input())
used = [0] * n
dfs(v - 1)