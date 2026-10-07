d = int(input())
n = int(input())
a = int(input())
b = int(input())
c = int(input())
if (d == 1):
    if a + b + c > n:
        print((a + b + c) % n)
    else:
        print(0)
else:
    print(min(a, b, c))

