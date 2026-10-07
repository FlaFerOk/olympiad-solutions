# počet tiav (najskôr skúsme pre N == 4)
from pickle import GLOBAL

N = 4
pamat_tiav = []
rozlozenie_tiav = []

# príprava údajových štruktúr
# čo všetko si musíme uložiť do pamäte?

#vytvoriť matice
def vytvoritMatice():
    for i in range(N):
        r = []
        for j in range(N):
            if i == 0:
                r.append(j + 1)
            elif j == 0:
                r.append(i + 1)
            else:
                r.append(0)
        rozlozenie_tiav.append(r)

    for i in range(N):
        r = []
        for j in range(N):
            if i - j == 1:
                r.append(False)
            elif i == j:
                r.append(False)
            else:
                r.append(True)
        pamat_tiav.append(r)
    return pamat_tiav, rozlozenie_tiav


# výpis riešenia
def vypisRiesenie(arr):
    for i in arr:
        print(*i, sep=' ')

# rekurzívna funkcia
def postavTavu(den, miesto):
    for i in range(N):
        if pamat_tiav[i][miesto - 1] == True:
            pass


# hlavný program
# začíname obsadením 2. miesta v 2. deň
# (prvé miesta v jednotlivé dni ako aj poradie v prvý deň je vhodné zafixovať)

vytvoritMatice()
postavTavu(2, 2)
#pamat_tiav[3][0] = False
vypisRiesenie(pamat_tiav)
vypisRiesenie(rozlozenie_tiav)
