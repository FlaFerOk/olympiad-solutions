a, b, c = map(int, input().split())
c2 = c * -1
x1 = (c - b) / a
x2 = (c2 - b) / a
print(f"{x1:.3f} {x2:.3f}")