def dfs(o):
    used[o] = 1
    for i in range(n):
        if g[o][i] == 1 and used[i] == 0:
            dfs(i)

n, s = map(int, input().split())

g = []

for i in range(n):
    g.append(list(map(int, input().split())))

used = [0] * n
dfs(0)
print(sum(used) == n)
