from collections import deque

jld = deque()
n = int(input())
mx = deque([0])
for i in range(n):
    a = int(input())
    if a == 0:
        jld.pop()
        mx.pop()
        print(mx[-1])
    else:
        jld.append(a)
        b = mx[-1]
        mx.append(max(a, b))