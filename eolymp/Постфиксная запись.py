from collections import deque

s = input().split()
n = deque()
for i in s:
    if i == "+":
        n.append(n.pop() + n.pop())
    elif i == "-":
        n.append(-n.pop() + n.pop())
    elif i == "*":
        n.append(n.pop() * n.pop())
    else:
        n.append(int(i))
print(n.pop())