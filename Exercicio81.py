lista = []
while True:
    num = int(input('Digite um número: ').strip())
    lista.append(num)
    continuar = str(input('Desejar continuar? [S/N] ').strip().upper())[0]
    if continuar in 'N':
        break
    while continuar not in 'SN': 
        print(f'Tente novamente.', end='')
        continuar = str(input('Desejar continuar? [S/N] ').strip().upper())[0]
        if continuar in 'N':
            break
        else:
            lista.append(num)
decrescente = sorted(lista, reverse=True)
print(f'Você digitou {len(lista)} números')
print(f'A lista em ordem decrescente {decrescente}')
if 5 in lista:
    print(f'O valor 5 está na lista.')
else: 
    print(f'O valor 5 não está na lista')