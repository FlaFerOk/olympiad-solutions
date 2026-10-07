for _ in range(int(input())):
    f = "YES"
    n, m = map(int, input().split())
    
    g = [[0] * n for i in range(n)]
    
    for i in range(m):
        a, b = map(int, input().split())
        g[a-1][b-1] = 1
        g[b-1][a-1] = 1
        
    for i in range(n):
        for j in range(i+1, n):
            for u in range(j+1, n):
                if i != j and i != u and j != u:
                    if g[i][j] + g[i][u] + g[u][j] == 2:
                        f = "NO"
                                            
    print(f)
