port sys

sys.setrecursionlimit(1100)


def f(i):
    if len(i) == 1:
        return i[-1]
    else:
        return i[-1] + " " + f(i[:-1])


input()
a = list(input().split())
print(f(a))