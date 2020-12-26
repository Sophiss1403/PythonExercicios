lista = []
par = list()
impar = list()
while True:
    num = int(input('Digite um número: ').strip())
    lista.append(num)
    continuar = str(input('Deseja continuar? ').strip().upper())[0]
    if continuar in 'N':
        break
    while continuar not in 'SN':
        print('Tente novamente ', end='')
        continuar = str(input('Deseja continuar? ').strip().upper())[0]
for valor in lista:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'''Lista digitada: {lista}
Lista de valores pares: {par}
Lista de valores ímpares: {impar}''')