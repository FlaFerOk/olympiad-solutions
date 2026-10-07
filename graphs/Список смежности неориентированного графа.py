n, m = map(int, input().split())

ss = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    ss[a-1].append(b)
    ss[b-1].append(a)
 
for i in ss:
    print(*sorted(i))



