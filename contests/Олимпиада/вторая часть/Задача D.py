n, l = map(int, input().split())
if l == 0:
    print(-1)
else:
    mch = 0
    while n != 1:
        i = l
        while 1:
            if n - i * 2 >= 0:
                n -= i
                mch += 1
                break
            i -= 1
print(mch - 1)
            