mod = 10 ** 9 + 7

h, w, a, b = map(int, input().split())

pipu = [[0] * w for i in range(h)]

for i in range(w):
    pipu[0][i] = 1

for i in range(h - a):
    pipu[i][0] = 1

for i in range(1, h - a):
    for j in range(1, w):
        pipu[i][j] = (pipu[i][j-1] + pipu[i-1][j]) % mod

for i in range(h - a, h):
    for j in range(b, w):
        pipu[i][j] = (pipu[i][j-1] + pipu[i-1][j]) % mod

print(pipu[-1][-1])







