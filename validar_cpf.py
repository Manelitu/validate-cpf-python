"""
CPF = 168.995.350-09
1 * 10 = 10 ------------- 1 * 11 = 11
6 * 9 = 54 -------------- 6 * 10 = 60
8 * 8 = 64 -------------- 8 * 9 = 72
9 * 7 = 63 -------------- 9 * 8 = 72
9 * 6 = 54 -------------- 9 * 7 = 63
5 * 5 = 25 -------------- 5 * 6 = 30
3 * 4 = 12 -------------- 3 * 5 = 15
5 * 3 = 15 -------------- 5 * 4 = 20
0 * 2 = 0  -------------- 0 * 3 = 0
                          0 * 2 = 0
        297               343
11 - (297 % 11) = 11    11 - (343 % 11) = 9
11 - 0 = 11
11 > 9 = 0 if > 9 = 0
Digit 1 = 0             Digit 2 = 9
"""

input_cpf = input("Input your CPF: ")
cpf = "{}.{}.{}-{}".format(input_cpf[:3], input_cpf[3:6], input_cpf[6:9], input_cpf[9:])
cpf_formated = []
count1, count2, sum1, sum2 = [10, 11, 0, 0]

for values in input_cpf:
    cpf_formated.extend(values)

cpf_formated = list(map(int, cpf_formated))

for values in cpf_formated[:-2]:
   sum1 += count1 * values
   count1 -= 1

for values in cpf_formated[:-1]:
    sum2 += count2 * values
    count2 -= 1

comparate1 = (11 - (sum1 % 11))
comparate2 = (11 - (sum2 % 11))

if comparate1 <= 9 and comparate1 == cpf_formated[-2]:
    if comparate2 <= 9 and comparate2 == cpf_formated[-1]:
        print(f'The cpf {cpf} is invalid')
    else: print(f'The cpf {cpf} is invalid')
else: print(f'The cpf {cpf} is invalid')

