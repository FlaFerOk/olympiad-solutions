def dfs(o):
    used[o] = 1
    for i in g[o]:
        if used[i] == 0:
            dfs(i)


for _ in range(int(input())):
    n, m = map(int, input().split())
    
    g = [[] for i in range(n)]
    
    for i in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    
    used = [0] * n
    mkd = 0
    
    for s in range(n):
        if used[s] == 0:
            ssm = sum(used)
            dfs(s)
            lsm = sum(used)
            mkd = max(lsm - ssm, mkd)
    
    print(mkd)