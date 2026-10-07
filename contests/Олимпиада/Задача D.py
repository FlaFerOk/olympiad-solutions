n, k = map(int, input().split())
cf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
otv = []
if n < k or k == 1:
    print("Impossible")
else:
    for i in range(k):
        otv.append(cf[i])
    i = 0
    for _ in range(n):
        if i == k:
            i = 0
        print(otv[i], end="")
        i += 1
    