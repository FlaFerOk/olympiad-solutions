n = int(input())

stv = []

for i in range(n):
    stv.append(sum(list(map(int, input().split()))))
    
print(*stv)