from collections import deque

sb = deque()
s = input()
ans = 'yes'
for i in s:
    if i in '[({':
        sb.append(i)
    elif i in "])}":
        if sb:
            if i == ")":
                if sb[-1] == "(":
                    sb.pop()
                else:
                    ans = 'no'
                    break
            elif i == "]":
                if sb[-1] == "[":
                    sb.pop()
                else:
                    ans = 'no'
                    break
            elif i == "}":
                if sb[-1] == "{":
                    sb.pop()
                else:
                    ans = 'no'
                    break
        else:
            ans = 'no'
            break
if sb:
    ans = 'no'
print(ans)