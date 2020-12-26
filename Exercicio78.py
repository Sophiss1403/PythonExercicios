lista = list()

for cont in range(0, 5):
    lista.append(int(input(f'Digite o {cont+1}º valor: ').strip()))
print(f'A lista de valores digitados é: {lista}')

print(f'O maior valor da lista é o valor {max(lista)}, nas posições ', end='')
for c, n in enumerate(lista):
    if n == max(lista):
        print(f'{c}...', end='')

print(f'\nO menor valor da lista é o valor {min(lista)}, nas posições ', end='')
for c, n in enumerate(lista):
    if n == min(lista):
        print(f'{c}...', end='')
