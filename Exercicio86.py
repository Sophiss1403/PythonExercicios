'''Crie um programa que 
crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta.'''

'''Eu acho que fiz errado o exercício:
'''
'''col = []
ln = []
for i in range(3):
    for num, pos in enumerate(range(3)):
        col.append(int(input(f'Número da posição [{i}, {pos}]: ')))
        
ln.append(col[:])
cont = 0
for elemt in ln:  # parece gambiarra
    for e in elemt:
        if cont % 3 == 0:
            print(f'\n[  {e}  ]', end='')
            cont += 1
        else:
            print(f'[{e}:^5]', end='')
            cont += 1
'''

'''RESOLUÇÃO OFICIAL: 
'''
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# interessante reparar que aqui cada subarray é uma linha dessa matriz

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}] '))

print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()    '''
