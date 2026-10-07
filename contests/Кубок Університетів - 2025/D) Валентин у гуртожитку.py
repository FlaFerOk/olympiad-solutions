k = int(input())
t = int(input())

t -= k * k - 1

if t > k:
    t -= k + 1
    print(k - t)
else:
    print(t - 1)