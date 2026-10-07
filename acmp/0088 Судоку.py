def str_true():
    for i in l:
        f = [0] * 101
        for j in i:
            if f[j] == 0:
                f[j] = 1
            else:
                return False
        if sum(f[:n ** 2 + 1]) != n ** 2:
            return False
    return True


def col_true():
    for i in range(n ** 2):
        f = [0] * 101
        for j in range(n ** 2):
            if f[l[j][i]] == 0:
                f[l[j][i]] = 1
            else:
                return False
        if sum(f[:n ** 2 + 1]) != n ** 2:
            return False
    return True


def skv_true():
    for t1 in range(0, n**2, n):
        for t2 in range(0, n**2, n):
            f = [0] * 101
            for i in range(n):
                for j in range(n):
                    if f[l[i + t1][j + t2]] == 0:
                        f[l[i + t1][j + t2]] = 1
                    else:
                        return False
            if sum(f[:n ** 2 + 1]) != n ** 2:
                return False
    return True


def syd_true():
    return str_true() and col_true() and skv_true()


n = int(input())
l = []
for i in range(n ** 2):
    a = list(map(int, input().split()))
    l.append(a)
print("Correct" if syd_true() else "Incorrect")
