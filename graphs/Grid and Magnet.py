from collections import deque

def bfs(s, a):
    g[s[0]][s[1]] == a
    q = deque()
    q.append(s)
    hod = 0
    while q:
        p = q.popleft()
        mh = [1, 0, -1, 0]
        mw = [0, 1, 0, -1]
        for u in range(4):
            if 0 <= p[0] + mh[u] < h and 0 <= p[1] + mw[u] < w:
                if g[p[0] + mh[u]][p[1] + mw[u]] == ".":
                    q.append([p[0] + mh[u], p[1] + mw[u]])
                    g[p[0] + mh[u]][p[1] + mw[u]] = a
                    hod += 1
                if g[p[0] + mh[u]][p[1] + mw[u]] == "+" and pos[p[0] + mh[u]][p[1] + mw[u]] == "-":
                    pos[p[0] + mh[u]][p[1] + mw[u]] = "+"
                    hod += 1
    return hod
                
        
        
        

h, w = map(int, input().split())
g = []
for i in range(h):
    g.append(list(input()))

for i in range(h):
    for j in range(w):
        if g[i][j] == "#":
            mh = [1, 0, -1, 0]
            mw = [0, 1, 0, -1]
            for u in range(4):
                if 0 <= i + mh[u] < h and 0 <= j + mw[u] < w and g[i + mh[u]][j + mw[u]] == ".":
                    g[i + mh[u]][j + mw[u]] = "+"
                    
a = 1
ans = [1]
for i in range(h):
    for j in range(w):
        if g[i][j] == ".":
            pos = []
            for i in range(h):
                pos.append(["-"] * w)
            ans.append(bfs([i, j], a))
            a += 1




print(max(ans))
#for i in range(h):
#    print(*pos[i])
    
#print()
#for i in range(h):
#    print(*g[i])
                
                
                
                