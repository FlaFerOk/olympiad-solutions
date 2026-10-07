#1.Когда не возможно вывести sum(a) > v + p
#2.Vasyl can do it! sum(a) <= v
#3.Petro can do it! sum(a) <= p
#4.They both can do it! sum(a) <= v and sum(a) <= p
#5.(1, 4), (4, 1), (3, 2), (2, 3)

f = True
a = list(map(int, input().split()))
v, p = map(int, input().split())
sm = sum(a)
if sum(a) > v + p:
    print("They can not do it!")
else:
    if sum(a) <= v and sum(a) <= p:
        print("They both can do it!")
    elif sum(a) <= v:
        print("Vasyl can do it!")
    elif sum(a) <= p:
        print("Petro can do it!")
    else:
        for i in range(5):
            if a[i] <= v and (sm - a[i]) <= p and f:
                print("They need to work together!")
                print(f'Vasyl: {i + 1}')
                print("Petro: ", end="")
                for y in range(5):
                    if y != i:
                        print(y + 1, end=" ")
                f = False
                break
            elif a[i] <= p and (sm - a[i]) <= v and f:
                print("They need to work together!")
                print("Vasyl: ", end="")
                for y in range(5):
                    if y != i:
                        print(y + 1, end=" ")
                print(f'Petro: {i + 1}')
                f = False
                break
                
        
        if f:
            for i in range(5):
                for j in range(5):
                    #print(f"{a[i] + a[j]} <= {v}, {sm - a[i]} <= {p}, {f}")
                    if i != j and a[i] + a[j] <= v and sm - a[i] - a[j] <= p and f:
                        print("They need to work together!")
                        print(f'Vasyl: {i + 1} {j + 1}')
                        print("Petro: ", end="")
                        for y in range(5):
                            if y != i and y != j:
                                print(y + 1, end=" ")
                        f = False
                        break
                    elif i != j and a[i] + a[j] <= p and sm - a[i] - a[j] <= v and f:
                        print("They need to work together!")
                        print("Vasyl: ", end="")
                        for y in range(5):
                            if y != i and y != j:
                                print(y + 1, end=" ")
                        print(f'Petro: {i + 1} {j + 1}')
                        f = False
        if f:
            print("They can not do it!")
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        