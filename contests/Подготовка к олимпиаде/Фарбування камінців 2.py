n = int(input())
a = list(map(int, input().split()))

l = [0] * (n + 1)
for i in a:
    l[i] += 1
ans = n

for j in range(n + 1):
    if l[j] != 0:
        b = a.copy()
        cnt = 0
        max_cl = j
        for i in range(n):
            if b[i] != max_cl:
                b[i] = max_cl
                if i + 1 <= n - 1:
                    b[i + 1] = max_cl
                cnt += 1
        ans = min(ans, cnt)
        l[max_cl] = 0
    
print(ans)