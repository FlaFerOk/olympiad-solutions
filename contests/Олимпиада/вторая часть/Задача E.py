n = int(input())
l = list(map(int, input().split()))
mins = 1000000000000
for x in range(-120 , 120):
    s = 0
    for a in l:
        s += (x - a) ** 2
    if s < mins:
        mins = s
print(mins)