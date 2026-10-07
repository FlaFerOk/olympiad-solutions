mod = 10 ** 9 + 7

h, w, a, b = map(int, input().split())

f_mod = [1] * (h + w)
p_mod = [1] * (h + w)

for i in range(1, (h + w)):
    f_mod[i] = (f_mod[i - 1] * i) % mod
    p_mod[i] = pow(f_mod[i], mod - 2, mod)

#print(f_mod)
#print(p_mod)

pref1 = []
for i in range(b, w):
    pref1.append(f_mod[(h - a - 1) + i] * p_mod[i] * p_mod[(h - a - 1)] % mod)

h2 = a - 1
# 3
w2 = w - b - 1
# 3 = 8 - 5
pref2 = []

for i in range(w2, -1, -1):
    # 6 = 4! / (2! * 2!)
    # 3 = 3! / (1! * 2!)
    # 1 = 2! / (0! * 2!)
    pref2.append(f_mod[h2 + i] * p_mod[i] * p_mod[h2] % mod)

#print(pref1)
#print(pref2)

ans = 0
for i in range(len(pref1)):
    ans += (pref1[i] * pref2[i]) % mod

print(ans % mod)
#336 + 252 +
#7 8 3 5
# 8 = i(5) + (h(7) - a(3) - 1)