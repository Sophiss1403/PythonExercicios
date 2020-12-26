lista = list()
while True:
    num = input('Digite um número: ').strip()
    continuar = str(input('Desejar continuar? [S/N] ').strip().upper())[0]
    while continuar not in 'SN':
        print(f'Tente novamente. ', end='')
        continuar = str(input('Desejar continuar? [S/N] ').strip().upper())[0]
    if num.isnumeric() is True:
        if num not in lista:
            lista.append(num)
    else:
        print('Tente novamente. ', end='')
        num = input('Digite um número: ').strip()
        if num.isnumeric() is True:
            if num not in lista:
                lista.append(num)
    if continuar in 'N':
        break
print(f'A lista de valores digitados foi: {sorted(lista)}')
