def gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y
    
    
#a = int(input())
#b = int(input())
d, x, y = gcd(10, 44)
print(d, x, y)