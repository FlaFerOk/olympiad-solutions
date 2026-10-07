#import sys
#input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = a[i] + a[i - 1]    
k = int(input())
for i in range(k):
    l, r = map(int, input().split())
    print(a[r] - a[l-1])