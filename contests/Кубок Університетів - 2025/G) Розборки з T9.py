# n = int(input())
# s = input()
# m = len(s)
#
# ans3 = m * (n - 1)
# m1 = m
#
# for i in range(1, m):
#     if s[i] == s[i-1]:
#         m1 -= 1
#
# ans1 = m1
# ans2 = (n + 1) * m1 - m1
#
# print(ans1 + ans2 + ans3)

n = int(input())
s = input()
m = len(s)

p = 0

for i in range(1, m):
    if s[i] == s[i-1]:
        p += 1

ans1 = m - p
ans2 = (n + 1) * (m - p) - (m - p)
ans3 = m * (n - 1) - p

print(ans1 + ans2 + ans3)



