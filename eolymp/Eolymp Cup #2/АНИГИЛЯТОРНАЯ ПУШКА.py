n, k = map(int, input().split())
a = list(map(int, input().split()))

if n == 1 or k == 1:
    print(0)
elif k == 2:
    u = a[0]
    for i in a:
        if u != i:
            print(-1)
            break
    else:
        print(0)
elif n == 2:
    if a[0] == a[1]:
        print(0)
    else:
        print(1)
else:
    u = {a[0]}
    for i in a:
        u.add(i)
    if len(u) == 1:
        print(0)
    elif len(u) < k:
        print(1)
    else:
        print(2)
    