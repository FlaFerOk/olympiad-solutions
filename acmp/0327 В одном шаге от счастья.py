def listeder(k):
    h = []
    while k > 10:
        h.append(k % 10)
        k //= 10
    h.append(k)
    return h


def bil(a):
    for i in a:
        j1 = listeder(i + 1)
        j2 = listeder(i - 1)
        if sum(j1[:3]) == sum(j1[3:]):
            print("Yes")
        elif sum(j2[:3]) == sum(j2[3:]):
            print("Yes")
        else:
            print("No")


n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
bil(l)