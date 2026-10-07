def fib(a):
    if pos_fib[a] != -1:
        return pos_fib[a]
    else:
        pos_fib[a] = fib(a - 1) + fib(a - 2)
        return pos_fib[a]
         


n = int(input())
pos_fib = [-1] * (n + 2)
pos_fib[0] = 0
pos_fib[1] = 1
fib(n)
print(pos_fib[-2])