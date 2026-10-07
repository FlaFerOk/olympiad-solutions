a = int(input())
mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
try:
    print(mes[a - 1])
except:
    print("Error")