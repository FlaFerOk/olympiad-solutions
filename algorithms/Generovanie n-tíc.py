# riešenie Úlohy 1
def vyhodnot(mas):
    sum = 300
    zlato = 0
    for i in range(len(mas)):
        if mas[i] == 1:
            if zlato == 0:
                zlato = sum / ceny[i]
                sum = 0
            else:
                sum = zlato * ceny[i]
                zlato = 0
    if zlato != 0:
        sum = zlato * ceny[-1]
    return sum


def generuj(mas, i):
    if i == len(mas):
        print(*mas, sep='', end=' ')
        zisk = vyhodnot(mas)
        print(f"- {zisk:.4f}")
        return
    mas[i] = 0
    generuj(mas, i+1)
    mas[i] = 1
    generuj(mas, i+1)



# riešenie Úlohy 2


# hlavný program
ceny = [57, 56, 54, 57]
a = [0] * len(ceny)
generuj(a, 0)

