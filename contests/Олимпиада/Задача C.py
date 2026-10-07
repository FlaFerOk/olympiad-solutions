w, h = map(int, input().split())
x1, y1  = map(int, input().split())
x2, y2  = map(int, input().split())
s = 0
if x1 == x2 and (x1 == 0 or x1 == w):
    print(abs(y1 - y2))
elif y1 == y2 and (y1 == 0 or y1 == h):
    print(abs(x1 - x2))
elif x1 == x2 and y1 == y2:
    print(0)
else:
    if x1 == w and y2 == h:
        print(abs(w - x2) + abs(h - y1))
    elif x2 == w and y1 == h:
        print(abs(w - x1) + abs(h - y2))
    elif x1 == w and y2 == 0:
        print(abs(w - x2) + abs(0 - y1))
    elif x2 == w and y1 == 0:
        print(abs(w - x1) + abs(0 - y2))
    elif x1 == 0 and y2 == h:
        print(abs(0 - x2) + abs(h - y1))
    elif x2 == 0 and y1 == h:
        print(abs(0 - x1) + abs(h - y2))
    elif x1 == 0 and y2 == 0:
        print(abs(0 - x2) + abs(0 - y1))
    elif x2 == 0 and y1 == 0:
        print(abs(0 - x1) + abs(0 - y2))
    else:
        if (x1 == 0 and x2 == w) or (x2 == 0 and x1 == w):
            print(min((y1 + y2 + w), (abs(h - y1) + abs(h - y2) + w)))
        elif (y1 == 0 and y2 == h) or (y2 == 0 and y1 == h):
            print(min((x1 + x2 + h), (abs(w - x1) + abs(w - x2) + h)))
