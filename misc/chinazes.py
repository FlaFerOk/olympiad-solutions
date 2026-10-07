n = int(input())
balanse = 0
f = "chinazes"

for i in range(n):
    a, b = input().split()
    b = int(b)
    if a == "earn":
        balanse += b
    else:
        balanse -=b
    if balanse < 0:
        f = "debt"
        
print(f)
        







