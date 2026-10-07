n = int(input())
a = list(map(int, input().split()))

m  = 10 ** 9 + 7

psm = [0]

for i in range(1, n + 1):
    psm.append(psm[-1] + a[i - 1])
  
#print(psm)
q = int(input())
for _ in range(q):
    s = 0
    l, r = map(int, input().split())
    l -= 1
    for i in range(l, r):
        #print(a[i], psm[r], psm[i+1])
        s += (a[i] * (psm[r] - psm[i+1]) % m)
    print(s % m)