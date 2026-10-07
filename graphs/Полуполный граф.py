for _ in range(int(input())):
    f = "YES"
    n, m = map(int, input().split())
    
    g = [[0] * n for i in range(n)]
    
    for i in range(m):
        a, b = map(int, input().split())
        if a != b:
            g[a-1][b-1] = 1
            g[b-1][a-1] = 1
    
    sm = 0
    for i in g:
        sm += sum(i)
    
    if sm != n * (n - 1):
        f = "NO"
        
    print(f)