for _ in range(int(input())):
    s = input()
    cps = 0
    ln = len(s)
    l = 0
    r = ln - 1
    len_ot = 1

    f = True
    while l < r:
        f = True
        if s[l] == s[r]:
            if s[l:l + len_ot] == s[r:r + len_ot]:
                cps += 2
                l += len_ot
                r -= 1
                len_ot = 1
                f = False
            else:
                r -= 1
                len_ot += 1
        else:
            r -= 1
            len_ot += 1

    ln = len(s)
    if ln % 2 != 0:
        cps += 1
    else:
        if f:
            cps += 1

    print(cps)

