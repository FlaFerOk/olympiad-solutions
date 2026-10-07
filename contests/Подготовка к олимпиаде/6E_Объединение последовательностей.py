k = int(input())
ab = []
i = 0
ai = 1
bi = 1
while i != k:
    ac = ai ** 2
    bc = bi ** 3
    if ac < bc:
        if ac != ab[-1]:
            ab.append(ac)
            i += 1
        ai += 1
    elif ac > bc:
        if bc != ab[-1]:
            ab.append(bc)
            i += 1
        bi += 1
    elif ac == bc:
        ab.append(ac)
        i += 1
        ai += 1
        bi += 1
print(ab[-1])