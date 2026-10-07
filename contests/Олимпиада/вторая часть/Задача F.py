n = int(input())
sy = list(map(int, input().split()))
q = int(input())
k = []
for i in range(q):
    k.append(int(input()))
sk = sorted(k)
sys = []
for i in range(sk[-1]):
    if i + 1 in sk:
        sys.append([i + 1, sy[0], sy[1]])
    mn = min(sy[0], sy[1])
    mx = max(sy[0], sy[1])
    sy[1:-1] = sy[2:]
    sy[0] = mx
    sy[-1] = mn
for i in k:
    for j in sys:
        if j[0] == i:
            print(j[1], j[2])