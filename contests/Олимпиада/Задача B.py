n, a, b = map(int, input().split())
n *= 100
v = a * 100 + b
s = (n // (v * 50))
print(s // 2, s % 2)