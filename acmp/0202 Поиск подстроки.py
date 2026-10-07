def chat_to_int(b):
    return ord(b) - 96

def H(s, p, m):
    l = len(s)
    hash = 0

    for i in range(1, l + 1):
        hash += p ** (l - i) * chat_to_int(s[i - 1])

    return hash % m



def p(n, p, m):
    P = [1]
    for i in range(1, n):
        P.append((P[-1] * p) % m)
    return P


def h(s, p, m):
    hm = [H(s[:1], p, m)]
    for i in range(1, len(s)):
        hm.append((hm[-1] * p + chat_to_int(s[i])) % m)
    return hm


def get_hash(hm, P, l, r, m):
    if l == 0:
        return hm[r]
    else:
        return ((hm[r] - hm[l - 1]) * P[r - l + 1]) % m


s = input()
t = input()

hm = h(s, 101, 10*9+7)
ht = H(t, 101, 10*9+7)

ans = []
lt = len(t)
ls = len(s)
P = p(ls, 101, 10*9+7)

print(P)
print(hm)
print(ht)
print(get_hash(hm, P, 5, 7, 10*9+7))


for i in range(ls - lt):

    if get_hash(hm, P, i, i + lt - 1, 10*9+7) == ht:
        ans.append(i)

print(*ans)
