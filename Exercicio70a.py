maior = menor = quant = soma = mais_de_mil = 0
continuar = ' '
nome_barato = ' '
while True:
    nome = str(input('Produto: ').strip())
    preco = float(input('Preço do produto: R$').replace('.', ','))
    soma += preco
    quant += 1
    continuar = str(input('Quer continuar?')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?')).strip().upper()[0]
    if continuar in 'N':
        break
    if quant == 1:
        maior = menor = preco
        nome_barato = nome
    else:
        if preco > maior:
            maior = preco
        else:
            menor = preco
            nome_barato = nome
    if preco > 1000:
        mais_de_mil += 1
print(f'''O total gasto na compra foi de {soma}.
Foram comprados {mais_de_mil} produtos custando mais de R$1000,00.
O nome do produto mais barato é: {nome_barato} que custa R${menor}''')
