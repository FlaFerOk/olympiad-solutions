from collections import deque

l = deque()
size = 0
while 1:
    s = list(input().split())
    if s[0] == "push_back":
        l.append(int(s[1]))
        size += 1
        print("ok")
    
    elif s[0] == "push_front":
        l.appendleft(int(s[1]))
        size += 1
        print("ok")
        
    elif s[0] == "front":
        if size > 0:
            print(l[0])
        else:
            print("error")
    
    elif s[0] == "back":
        if size > 0:
            print(l[-1])
        else:
            print("error")
    
    elif s[0] == "size":
        print(size)
    
    elif s[0] == "clear":
        l.clear()
        size = 0
        print("ok")
    
    elif s[0] == "exit":
        print('bye')
        break
    
    elif s[0] == "pop_back":
        if size > 0:
            print(l[-1])
            l.pop()
            size -= 1
        else:
            print("error")
            
    else:
        if size > 0:
            print(l[0])
            l.popleft()
            size -= 1
        else:
            print("error")
