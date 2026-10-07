def pow_(x, n):
    if n == 1:
        return x
    elif n % 2 != 0:
        return x * pow_(x, n - 1)
    else:
        a = pow_(x, n // 2)
        return a * a


n = int(input())
print(pow_(2, n))