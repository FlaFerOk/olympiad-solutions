# rozmer šachovnice
N = 6
pocetreheni = 0

# vytvorenie šachovnice
sach = [[0]*N for i in range(N)]

# relatívne posuny v stlpcoch a riadkoch pri skákaní
ds = [1, 2, 2, 1, -1, -2, -2, -1]
dr = [-2, -1, 1, 2, 2, 1, -1, -2]

# pomocná funkcia na výpis riešenia
def vypis_riesenie():
    for i in range(N):
        for j in range(N):
            print(f'{sach[i][j]:3d}', end='')
        print()
    print('------------')

# pomocná funkcia na overenie dostupnosti políčka
def je_volne(r,s):
    return 0<=r<N and 0<=s<N and sach[r][s]==0
    
# rekurzívna funkcia
def skac(krok, r, s):
    global pocetreheni
    if not je_volne(r, s): return
    sach[r][s] =  krok
    if krok == N*N:
        pocetreheni = pocetreheni + 1
        vypis_riesenie()
    else:
        for i in range(8):
            skac(krok+1, r+dr[i], s+ds[i])
    sach[r][s] = 0
    
# hlavný program
skac(1, 0, 0)
print(pocetreheni)