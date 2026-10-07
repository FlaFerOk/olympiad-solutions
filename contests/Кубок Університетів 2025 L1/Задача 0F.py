x = float(input())
sm = 1
i = 2
while x > sm:
    sm += 1 / i
    sm = round(sm, 6)

print(i - 1, i)