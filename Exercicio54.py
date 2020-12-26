import datetime

cont_maior = 0  # contando pessoas maiores de idade
cont_menor = 0  # contando pessoas menores de idade
for contador in range(0, 7):  # tudo isso é feito 7 vezes
    ano = int(input('Digite o ano em que você nasceu: '))  # pedindo 7 anos de nascimento
    atual = datetime.date.today()  # salvando o ano atual
    dif = atual.year - ano  # subtraindo o ano atual do ano de nascimento
    if dif >= 21:  # se a diferença for maior ou igual a 21
        cont_maior += 1  # é contado mais um
    elif dif <= 21:  # se a diferença for menor ou igual a 21
        cont_menor += 1  # é contado mais um na variável correspondente

print('Foram computadas:'
      '\n- {} pessoas com 21 anos ou mais;'
      '\n- {} pessoas com menos de 21 anos.'.format(cont_maior, cont_menor))  # imprimindo dados
