col = []
ln = []

for i in range(3):
    for num, pos in enumerate(range(3)):
        col.append(int(input(f'Número da posição [{i}, {pos}]: ')))
        
ln.append(col[:])
cont = 0
for elemt in ln:  # parece gambiarra
    for e in elemt:
        if cont % 3 == 0:
            print(f'\n[{e:^5}]', end='')
            cont += 1
        else:
            print(f'[{e:^5}]', end='')
            cont += 1

pares = []
for e in elemt:
    if e % 2 == 0:
        pares.append(e)
print()
print('-=' * 30)
col3 = [col[2], col[5], col[8]]
print(f'Valores pares: {pares}, cuja soma é {sum(pares)}.')
print('-=' * 30)
print(f'3ª coluna: {col3}, cuja soma de valores resulta em {sum(col3)}.')
print('-=' * 30)
ln2 = [ln[0][3], ln[0][4], ln[0][5]]
ln2.sort()
print(f'O maior valor da 2ª linha é: {ln2[-1]}')
