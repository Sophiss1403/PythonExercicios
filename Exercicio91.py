from time import sleep
import random
from operator import itemgetter

jogadores = {
'jogador1' : random.randint(1,6),
'jogador2' : random.randint(1,6),
'jogador3' : random.randint(1,6),
'jogador4' : random.randint(1,6) }

ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-'* 30)
for jogador, dado in jogadores.items():
    print(f'O {jogador} tirou {dado} no dado.')
    sleep(1)
print('-'* 30)

print(f'{"== RANKING ==":>20}')

for i, pos in enumerate(ranking):
    print(f'{i+1}º colocado: {pos[0]} com {pos[1]}')
    sleep(1)
print('-'* 30)
