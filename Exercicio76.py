# in order to activate the interactive mode, uncomment the lines below:

'''tabela = (str(input('Digite o produto: ')), float(input('Digite o preço: R$').strip()),
         str(input('Digite o produto: ')), float(input('Digite o preço: R$').strip()),
         str(input('Digite o produto: ')), float(input('Digite o preço: R$').strip()),
          str(input('Digite o produto: ')), float(input('Digite o preço: R$').strip()))'''

tabela = ('Macarrão', 3.90,
          'Massa de Tomate' , 2.20,
          'Temperos Variados', 5.00,
          'Refrigerante', 7.90,
          'Carne Moída', 15,
          'Água Mineral (1 litro)', 5.50)

titulo = 'LISTA DE COMPRAS'

print('-'*60)
print(titulo.center(60))
print('-'*60)
for item in tabela:
    if type(item) == str:
        print(f'{item:.<45s}', end='')
    elif type(item) == float or int:
        print(f'R$ {item:>5.2f}')
print('-'*60)
