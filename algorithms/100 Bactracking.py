def count_of_sums(i):
    global cislo, count
    if i >= len(cislo):
        if eval(cislo) == 100:
            count += 1
        return

    if i == 1:
        count_of_sums(i+1)
    elif cislo[i-1] != "0" or cislo[i-2] != "-" and cislo[i-2] != "+":
        count_of_sums(i+1)
    cislo = cislo[:i] + "+" + cislo[i:]
    count_of_sums(i+2)
    cislo = cislo[:i] + "-" + cislo[i+1:]
    count_of_sums(i+2)
    cislo = cislo[:i] + cislo[i + 1:]

cislo = input()
count = 0
count_of_sums(1)
print(count)