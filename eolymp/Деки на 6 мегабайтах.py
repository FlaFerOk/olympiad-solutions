from collections import deque

n = int(input())
dek_dek = [0] * 1000000
for _ in range(n):
    deis = list(input().split())
    if deis[0] == "pushback":
        a = int(deis[1]) -1
        if dek_dek[a] == 0:
            dek_dek[a] = deque()
        dek_dek[a].append(deis[2])
    elif deis[0] == "pushfront":
        a = int(deis[1]) -1
        if dek_dek[a] == 0:
            dek_dek[a] = deque()
        dek_dek[a].appendleft(deis[2])
    elif deis[0] == "popback":
        print(dek_dek[int(deis[1])-1].pop())
    elif deis[0] == "popfront":
        print(dek_dek[int(deis[1])-1].popleft())
