def mergesort(mas):
    if len(mas) == 1:
        return mas
    mid = len(mas) // 2
    return merge(mergesort(mas[:mid]), mergesort(mas[mid:]))


def merge(a, b):
    ia = 0
    ib = 0
    ab = []
    while ia < len(a) and ib < len(b):
        if a[ia] < b[ib]:
            ab.append(a[ia])
            ia += 1
        else:
            ab.append(b[ib])
            ib += 1
    return ab + a[ia:] + b[ib:]


print(mergesort([3, 6, 7, 10, 15, 1, 4, 5, 7, 11, 22, 30]))
            