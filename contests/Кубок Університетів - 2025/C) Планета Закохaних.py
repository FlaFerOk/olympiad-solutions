n = int(input())
k = int(input())

if k % 2 == 0:
    print(0)
else:
    print(((k // 2 + n * 2) // 7) - 1)

# c = 0
#
# for i in range(n):
#     if k == 5:
#         c += 1
#     k = (k + 2) % 7
#
# print(c)