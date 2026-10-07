def f(a):
    while a % 2 == 0:
            a //= 2
    while a % 3 == 0:
            a //= 3
    if a == 1:
        return "Yes"
    return "No"


n = int(input())
print(f(n))


