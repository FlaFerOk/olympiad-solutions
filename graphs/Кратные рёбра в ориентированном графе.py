for _ in range(int(input())):
    f = "NO"
    n, m = map(int, input().split())
    
    g = [[0] * n for i in range(n)]
    
    for i in range(m):
        a, b = map(int, input().split())
        if g[a-1][b-1] == 1:
            f = "YES"
        g[a-1][b-1] += 1
        
    print(f)
    
            
            

