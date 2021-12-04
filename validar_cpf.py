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

