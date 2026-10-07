n = int(input())
a = list(map(int, input().split()))
S = sum(a)

ans = 1

target = 0
for x in a:
    target += x
    parts = 0
    curr = 0
    f = True

    if S % target != 0:
       continue

    for i in a:
        curr += i
        if curr == target:
            parts += 1
            curr = 0
        elif curr > target:
            f = False
            break

    if f and curr == 0:
        if parts > ans:
            ans = parts

print(ans - 1)


