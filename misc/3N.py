n = int(input())
a = list(map(int, input().split()))
vh = list()
j = 0
for i1 in range(1, n + 1):
    for i in range(3 * n):
        if a[i] == i1:
            j += 1
            if j == 2:
                vh.append(i + 1)
                j = 0
                break
print(vh)



