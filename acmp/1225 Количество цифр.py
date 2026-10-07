def is_digit(y):
    return y in "0123456789"


a = list(input().split())
s = 0
for i in a:
    s += is_digit(i)
print(s)