from collections import deque

int(input())
p = deque(map(int, input().split()))
t = deque()
f = [0]

while p:
    t.append(p[0])
    p.popleft()
    while t and (t[-1] == f[-1] + 1):
        f.append(t[-1])
        t.pop()
if t:
    print("NO")
else:
    print("YES")