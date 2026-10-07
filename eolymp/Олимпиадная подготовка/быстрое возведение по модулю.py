def pow_(x, n, mod):
    if n == 1:
        return x % mod
    elif n % 2 != 0:
        return (x * pow_(x, n - 1, mod)) % mod 
    else:
        a = pow_(x, n // 2, mod)
        return (a * a) % mod


a, b, m = map(int, input().split())
print(pow_(a, b, m))