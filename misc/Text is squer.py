file = open("input.txt", "r")
lines = []
max_len = 0
for i in file:
    lines.append(i.strip("\n"))
    if len(i) > max_len:
        max_len = len(i)

print("*" * (max_len + 2))
flag = True
for i in range(len(lines)):
    count_of_space = max_len - len(lines[i])
    if count_of_space % 2 == 0:
        print("*" + (count_of_space // 2 * " ") + lines[i] + (count_of_space // 2 * " ") + "*")
    else:
        if flag:
            print("*" + (count_of_space // 2 * " ") + lines[i] + (count_of_space // 2 * " ") + " *")
            flag = False
        else:
            print("* " + (count_of_space // 2 * " ") + lines[i] + (count_of_space // 2 * " ") + "*")
            flag = True
print("*" * (max_len + 2))