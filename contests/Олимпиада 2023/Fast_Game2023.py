pch = [[0], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
a, b = map(int, input().split())
a = a % 10
if b == 0:
    print(1)
else:
    print(pch[a][b % len(pch[a])])