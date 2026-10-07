def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d += 2
    return True


def fib(a):
    if f_list[a] != -1:
        return f_list[a]
    else:
        f_list[a] = fib(a - 1) + fib(a - 2)
        return f_list[a]
    
    
n = int(input())
f_list = [-1] * (n + 1)
f_list[0] = 0
f_list[1] = 1
fib(n)
print(f_list[-1])

    