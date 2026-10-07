S = input()
F = input()
x = ord(F[0]) - 97 - (ord(S[0]) - 97) 
y = (8 - int(F[1:])) - (8 - int(S[1:]))
ans = []
while x or y:
    xy = ""
    if x > 0:
        xy += "R"
        x -= 1
    elif x < 0:
        xy += "L"
        x += 1
    if y > 0:
        xy += "D"
        y -= 1
    elif y < 0:
        y += 1
        xy += "U"
    ans.append(xy)
    
print(len(ans))
for i in ans:
    print(i)