n, m = map(int, input().split())

svg = [[0] * 2 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    svg[a - 1][1] += 1
    svg[b - 1][0] += 1
    
for i in svg:
    print(*i)