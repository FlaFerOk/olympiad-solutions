def hard_math_sum(a_sum, b_sum):
    a_sum = a_sum.zfill(max(len(a_sum), len(b_sum)))
    b_sum = b_sum.zfill(max(len(a_sum), len(b_sum)))
    
    a_sum = a_sum[::-1]
    b_sum = b_sum[::-1]
    c_sum = ""
    s_sum = 0
    for i in range(len(a_sum)):
        c_sum += str((int(a_sum[i]) + int(b_sum[i]) + s_sum) % 10)
        s_sum = (int(a_sum[i]) + int(b_sum[i]) + s_sum) // 10
    if s_sum:
        c_sum += '1'
    return c_sum[::-1]


a = input()
b = input()
c = hard_math_sum(a, b)
print(c)