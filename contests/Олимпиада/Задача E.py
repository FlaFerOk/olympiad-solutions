n = int(input())
a = list(map(int, input().split()))
mx = [0, 0]
mn = [a[0], 0]
for i in range(n):
    if a[i] > mx[0]:
        mx[0] = a[i]
        mx[1] = i
    if a[i] <= mn[0]:
        mn[0] = a[i]
        mn[1] = i
if mx[1] < mn[1]:
    print((mx[1]) + (n - mn[1] - 1))
else:
    print((mx[1]) + (n - mn[1] - 1) - 1)
        