n = int(input())
mvk = [0, 0]
for i in range(n+1):
    for j in range(n+1):
        vk = (i ^ j)+(i | j)+(i & j)
        if vk == mvk[0]:
            mvk[1] += 1
        else:
            if vk > mvk[0]:
                mvk[0] = vk
                mvk[1] = 1
print(*mvk)