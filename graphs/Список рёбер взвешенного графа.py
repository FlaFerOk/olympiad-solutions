n, m = map(int, input().split())

sm = 0
mx = [0, 0, 0]
mn = [99999999999999999999999999999999999999999999999999999999999999999999999999999999, 0, 99999999999999999999999999999999999999999999999999999999999999999999999999999999]

for i in range(m):
    a, b, c = map(int, input().split())
    sm += c
    if c >= mx[2]:
        mx[0] = a
        mx[1] = b
        mx[2] = c
    if c < mn[2]:
        mn[0] = a
        mn[1] = b
        mn[2] = c

print(sm)
print(*mx)
print(*mn)

