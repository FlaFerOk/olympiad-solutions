for _ in range(int(input())):
    f = "YES"
    n = int(input())
    
    g = []
    for i in range(n):
        g.append(list(map(int, input().split())))
        
    for i in range(n):
        if g[i][i] == 1:
            f = "NO"
        
    for i in range(n):
        for j in range(i + 1, n):
            if g[i][j] != g[j][i]:
                f = "NO"
                
    print(f)
            
            