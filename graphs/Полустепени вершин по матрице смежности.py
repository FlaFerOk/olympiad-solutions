n = int(input())

svg = [[0] * 2 for i in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 1:
            svg[j][0] += 1
            svg[i][1] += 1
    
for i in svg:
    print(*i)