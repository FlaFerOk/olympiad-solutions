n = int(input())
d = list(map(int, input().split()))
sm = 0
for i in range(1, n + 1):
    if len(set(list(str(i)))) == 1:
        a = i % 10
        if d[i - 1] >= a:
            sm += 1
        if d[i - 1] >= (a + (a * 10)):
            sm += 1
print(sm)


