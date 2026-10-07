import heapq

def f(sub, m, k):
    L = len(sub)
    I = min(m, L)

    heap = sub[:I]
    heapq.heapify(heap)

    for i in range(1, k + 1):
        x = heapq.heappop(heap)
        if i == k:
            return x
        if I < L:
            heapq.heappush(heap, sub[I])
            I += 1


n, q = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q):
    l, r, m, k = map(int, input().split())
    sub = a[l-1:r]
    print(str(f(sub, m, k)), end="\n")
