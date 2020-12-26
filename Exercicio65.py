num = int(input('Digite um número inteiro: ').strip())
soma = 0
cont = 0
soma += num
cont += 1
continuar = ''
lista = list()
lista.append(num)
maior = sorted(lista)
menor = sorted(lista, reverse=True)
while continuar != 'N':
    continuar = str(input('Deseja continuar? [S/N]').strip().upper())
    if continuar == 'N':
        break
    else:
        num = int(input('Digite um número inteiro').strip())
        lista.append(num)
        soma += num
        cont += 1
        maior = sorted(lista)
        menor = sorted(lista, reverse=True)
print('''O número de valores digitados foi: {}
A média dos valores digitados foi: {}
O maior valor digitado foi: {}
O menor valor digitado foi: {}'''.format(cont, soma/cont, str(maior[-1]), str(menor[-1])))
