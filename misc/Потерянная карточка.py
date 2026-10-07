a = list(map(int, input().split()))
print(abs(sum(a) - a[0] - ((a[0] + 1) * a[0]) // 2))