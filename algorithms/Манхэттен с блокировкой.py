class Manhattan_with_a_lock:
    def __init__(self, args_xy, blocked):
        self.chenge_xy(args_xy)
        self.chenge_blocked(blocked)
        self.calculate_mapu()


    def chenge_xy(self, args):
        self.__x, self.__y = map(int, args.split(','))


    def chenge_blocked(self, blocked):
        self.__blocked = blocked


    def calculate_mapu(self):
        self.__mapa = []
        for i in range(self.__x + 1):
            r = []
            for j in range(self.__y + 1):
                if [i, j] in self.__blocked:
                    r.append(0)
                elif j == 0 or i == 0:
                    if j == 0 and i > 0 and self.__mapa[i-1][0] == 0:
                        r.append(0)
                    elif i == 0 and j > 0 and r[j-1] == 0:
                        r.append(0)
                    else:
                        r.append(1)
                else:
                    r.append(-1)
            self.__mapa.append(r)

        for i in range(1, self.__x + 1):
            for j in range(1, self.__y + 1):
                if self.__mapa[i][j] < 0:
                    self.__mapa[i][j] = self.__mapa[i - 1][j] + self.__mapa[i][j - 1]


    def print_map(self):
        for i in range(self.__x, -1, -1):
            print(*self.__mapa[i])

    def print_value_xy(self):
        print(self.__mapa[self.__x][self.__y])



xy = input()
blocked = []
for i in range(int(input())):
    blocked.append(list(map(int, input().split(','))))

manhattan = Manhattan_with_a_lock(xy, blocked)
manhattan.calculate_mapu()
#manhattan.print_map()
manhattan.print_value_xy()

"""
tests:
n1:
vstup:
8,15
5
6,7
6,9
1,5
2,12
8,4
vystup: 223517  

n2:
vstup:
7,8
3
5,6
6,7
1,1
vystup: 999

n3: 
vstup:
9,17
2
5,8
8,11
vystup: 1855451
"""

"""
x, y = map(int, input().split(','))

blocked = []
for i in range(int(input())):
    blocked.append(list(map(int, input().split(','))))

mapa = []
for i in range(x + 1):
    r = []
    for j in range(y + 1):
        if [i, j] in blocked:
            r.append(0)
        elif j == 0 or i == 0:
            if j == 0 and i > 0 and mapa[i-1][0] == 0:
                r.append(0)
            elif i == 0 and j > 0 and r[j-1] == 0:
                r.append(0)
            else:
                r.append(1)
        else:
            r.append(-1)
    mapa.append(r)

for i in range(1, x + 1):
    for j in range(1, y + 1):
        if mapa[i][j] < 0:
            mapa[i][j] = mapa[i-1][j] + mapa[i][j-1]

print(mapa[x][y])
"""