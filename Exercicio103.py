'''Esse exercício é sobre parâmetros opcionais em funções

Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. 
'''


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Gols: '))
if g.isnumeric():   # .isdecimal é melhor pq isnumeric cria um bug
    g = int(g)
else:
    g = 0
if n.strip() == '':  # muito boa a escolha pelo strip, já trata a possiblidade da pessoa digitar vários espaços
    ficha(gol=g)
else:
    ficha(n, g)
