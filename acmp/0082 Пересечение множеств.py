n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = [0]*(10 ** 5 + 1 )
for i in a:
    l[i] = 1
for i in b:
    if l[i] == 1:
        l[i] = 2
for i in range (10 ** 5 + 1):
    if l[i] == 2:
        print(i, end=' ')