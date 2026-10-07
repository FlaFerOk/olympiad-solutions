import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)


def dfs(o):
    used[o] = 1
    ks.append(o + 1)
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
v = []
    
for s in range(n):
    if used[s] == 0:
        ks = []
        dfs(s)
        v.append(ks)

print(len(v))
for i in v:
    print(len(i))
    print(*i)
