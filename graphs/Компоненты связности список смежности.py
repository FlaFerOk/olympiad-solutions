import sys
sys.setrecursionlimit(100000)


def dfs(o):
    used[o] = 1
    for i in g[o]:
        if used[i] == 0:
            dfs(i)


n = int(input())
g = [[] for i in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    for j in a[1:]:
        g[i].append(j-1)
  
used = [0] * n
ks = 0

for i in range(n):
    if used[i] == 0:
        dfs(i)
        ks += 1

print(ks)