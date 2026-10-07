for _ in range(int(input())):
    f = "YES"
    n, m = map(int, input().split())
    
    g = [0] * n
    
    for i in range(m):
        a, b = map(int, input().split())
        g[a-1] += 1
        g[b-1] += 1
        
    if len(set(g)) != 1:
        f = "NO"
        
    print(f)