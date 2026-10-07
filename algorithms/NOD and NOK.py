def NOD(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    elif a >= b:
        return NOD(a % b, b)
    else:
        return NOD(a, b % a)


for i in range(1000):
    a = int(input())
    if a == 0:
        break
    c = 0
    for i in range(1, a):
        if NOD(i, a) == 1:
            c += 1
    print(c)

            


