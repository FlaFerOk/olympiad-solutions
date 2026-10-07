n = int(input())
l = [0] * 10
for i in range(1, n + 1):
    while i != 0:
        l[i % 10] += 1
        i //= 10
print(*l)