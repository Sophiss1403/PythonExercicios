'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados e um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from time import sleep
import random
from operator import itemgetter

jogadores = {
'jogador 1' : random.randint(1,6),
'jogador 2' : random.randint(1,6),
'jogador 3' : random.randint(1,6),
'jogador 4' : random.randint(1,6) }
#---- 0 --------- 1 ------------- 
# ordena (por padrão decrescente) da forma correta, relacionando o jogador e o dado:

ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # o 1 representa a coluna 1, dos valores
# se fosse 0 ao invés de 1, representaria e ordenaria pelas chaves

# ordenada = list(jogadores.values())
# ordenada.sort() --> assim é possível ordenar os valores, mas não ordena relacionando o jogador e o valor

print('-'* 30)
for jogador, dado in jogadores.items():
    print(f'O {jogador} tirou {dado} no dado.')
    sleep(1)
print('-'* 30)


print(f'{"== RANKING ==":>20}')

for i, pos in enumerate(ranking):
    print(f'{i+1}º colocado: {pos[0]} com {pos[1]}')
