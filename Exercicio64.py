num = int(input('Digite um número até 999: '))  # peço o primeiro número
soma = 0  # acumulador
cont = 1  # contador
soma += num  # acumulo o primeiro número
while num != 999:  # enqt o num n for igual ao da condição de parada
    num = int(input('Digite um número até 999: '))  # peço mais números
    if num == 999:  # se receber 999
        break  # para e vai pra fora do laço
    else:  # do contrario
        soma += num  # acumula o número
        cont += 1  # e conta mais um
print('A soma dos {} valores digitados foi de: {}'.format(cont, soma))
