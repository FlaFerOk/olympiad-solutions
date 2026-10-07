def deli(a):
    dl = []
    d = 2
    while d * d <= a:
        f = 0
        while a % d == 0:
            a = a // d
            f+=1
        if f != 0:
            dl.append(d)
        d+=1
    if a != 1:
        dl.append(a)
    return dl


for i in range(1000):
    n = int(input())
    if n == 0:
        break
    del_ = deli(n)
    for j in del_:
        n = n * (1 - 1/j)
    print(int(n))
    
    
    
    
    
