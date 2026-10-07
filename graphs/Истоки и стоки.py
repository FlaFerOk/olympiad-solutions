n = int(input())

g = []

ist = [0]
st = [0]

for i in range(n):
    g.append(list(map(int, input().split())))

for i in range(n):
    it = 0
    s = 0
    for j in range(n):
        s += g[i][j]
        it += g[j][i]
    if it == 0:
        ist[0] += 1
        ist.append(i+1)
    if s == 0:
        st[0] += 1
        st.append(i+1)
        
print(*ist)
print(*st)
        