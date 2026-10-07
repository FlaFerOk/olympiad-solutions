import sys
sys.setrecursionlimit(100000)


def dfs(o):
    used[o] = 1
    for i in g[o]:
        if used[i] == 0:
            dfs(i)
            

n, m = list(map(int, input().split()))

g = [set() for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].add(b-1)
    g[b-1].add(a-1)

used = [0] * n
mnkd = 9999999999999999999999999999999999999999999999999999999999999999999999
mkd = 0
    
for s in range(n):
    if used[s] == 0:
        ssm = sum(used)
        dfs(s)
        lsm = sum(used)
        mkd = max(lsm - ssm, mkd)
        mnkd = min(lsm - ssm, mnkd)

print(mnkd, mkd)