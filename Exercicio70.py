"""C) Qual é o nome do produto mais barato."""
produtos = list()
pre_pro = list()
continuar = ' '
nome_barato = ' '
while True:
    nome = str(input('Produto: ').strip())
    produtos.append(nome)
    preco = float(input('Preço do produto: R$').replace('.', ','))
    pre_pro.append(preco)
    continuar = str(input('Quer continuar?').strip().upper())
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?').strip().upper())
    if continuar in 'N':
        break
mais_de_mil = [preco for preco in pre_pro if preco > 1000]
print(f'''O total gasto na compra foi de {sum(pre_pro)}
Foram comprados {len(mais_de_mil)} produtos custando mais de R$1000,00 
''')
print('Fim')
'''pego a lista de precos
anoto os indexes
ordeno do menor pro maior
vejo onde o index [0] estava antes de ser ordenado
o index de onde ele estava antes é o index do nome do produto mais barato
daí eu printo o nome mais barato pelo index de antes de ser ordenado o preco
'''