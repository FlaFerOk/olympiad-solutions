def dfs(o):
    used[o] = 1
    for i in g[o]:
        if used[i] == 0:
            dfs(i)


n, m = map(int, input().split())

g = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
  
used = [0] * n
dfs(0)
if sum(used) == n:
    print("YES")
else:
    print("NO")