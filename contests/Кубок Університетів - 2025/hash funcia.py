from math import pow

def chat_to_int(b):
    return ord(b) - 96

def H(s, p, m):
    l = len(s)
    hash = 0

    for i in range(1, l + 1):
        hash += p ** (l - i) * chat_to_int(s[i - 1])

    return hash % m

def h(s, p, m):
    hm = []
    for i in range(1, len(s) + 1):
        hm.append(H(s[:i], p, m))
    return hm


def p(n, p, m):
    P = [1]
    for i in range(1, n):
        P.append((P[-1] * p) % m)
    return P


def h1(s, p, m):
    hm = [H(s[:1], p, m)]
    for i in range(1, len(s)):
        hm.append((hm[-1] * p + chat_to_int(s[i])) % m)
    return hm


def get_hash(hm, P, l, r, m):
    if l == 0:
        return hm[r]
    else:
        return ((hm[r] - hm[l - 1]) * P[r - l + 1]) % m


print(h1("ababb", 3, 17))
for i in ["a", "ab", "aba", "abab", "ababb"]:
    print(i, h(i, 101, 10 ** 9 + 7))

    
    