from math import sqrt
def side(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) 


x1, y1, x2, y2, x3, y3 = map(int, input().split())
points = [[x1, y1], [x2, y2], [x3, y3]]
s = []
s.append(side(points[0], points[1]))
s.append(side(points[0], points[2]))
s.append(side(points[1], points[2]))
p = sum(s) / 2
y = sqrt(p * (p - s[0]) * (p - s[1]) * (p - s[2]))
if int(y) == y:
    print(int(y))
else:
    print(y)
