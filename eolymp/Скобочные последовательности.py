from collections import deque

q = deque()
s = input()
ans = 'YES'
for i in s:
    if i == '(':
        q.append(i)
    else:
        if q:
            q.pop()
        else:
            ans = 'NO'
            break
if q:
    ans = 'NO'
print(ans)