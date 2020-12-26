valores = tuple(int
                (input
                 ('Digite o {}º numero: '.format(valor)
                  )
                 ) for valor in range(1, 5))

print(f'Os valores digitados foram: {valores}')

print(f'O número 9 apareceu {valores.count(9)} vez(es).', end='\n')
if 3 in valores:
    print(f'A posição da primeira ocorrência do número três foi: {valores.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado')

print('Os valores pares digitados foram: ', end='')  # gambiarra feia demais
for valor in valores:
    if valor % 2 == 0:
        print(valor, end=' ')