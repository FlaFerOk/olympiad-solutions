for _ in range(int(input())):
    f = "YES"
    n, m = map(int, input().split())
    
    g = [[0] * n for i in range(n)]
    
    for i in range(m):
        a, b = map(int, input().split())
        g[a-1][b-1] = 1
        if g[b-1][a-1] != 0:
            f = "NO"
        
    if m != (n * (n - 1)) // 2:
        f = "NO"
        
    print(f)