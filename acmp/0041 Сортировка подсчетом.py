n = int(input())
a = list(map(int, input().split()))
l = [0] * 201
for i in a:
    l[i + 100] += 1

for i in range (201):
    if l[i] != 0:
        for _ in range(l[i]):
            print(i - 100, end=' ')