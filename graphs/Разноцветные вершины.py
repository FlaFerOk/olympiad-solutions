n = int(input())

g = []

for i in range(n):
    g.append(list(map(int, input().split())))
    
cvg = list(map(int, input().split()))

f = 0

for i in range(n):
    for j in range(i + 1, n):
        if g[i][j] == 1:
            if cvg[i] != cvg[j]:
                f += 1

print(f)