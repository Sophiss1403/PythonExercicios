num = int(input('Digite um número: ').strip())
cont = 1
soma = 0
soma += num
while True:
    num = int(input('Digite um número: ').strip())
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')
