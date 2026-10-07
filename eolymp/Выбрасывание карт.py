from collections import deque

while 1:
    n = int(input())
    if n != 0:
        D_cards = []
        a = deque(i for i in range(1, n + 1))
        while len(a) > 1:
            D_cards.append(a.popleft())
            a.append(a.popleft())
        print("Discarded cards: ", end="")
        print(*D_cards, sep=", ")
        print("Remaining card:", a.pop())
    else:
        break
    