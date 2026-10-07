for _ in range(int(input())):
    f = "YES"
    n = int(input())
    
    g = []
    
    for i in range(n):
        g.append(list(map(int, input().split())))
        
    for u in range(n):
        for v in range(n):
            for w in range(n):
                if u != v and u != w and v != w:
                    if g[u][v] and g[v][w] and not g[u][w]:
                        f = "NO"
                                            
    print(f)