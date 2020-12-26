from random import randint
from time import sleep

user = int(input('''Vamos jogar jokenpô!
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
DIGITE SUA OPÇÃO: ''').strip())
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
pc = randint(0, 2)
item = ('PEDRA', 'PAPEL', 'TESOURA')
print('O computador escolheu {}'.format(item[pc]))
print('O jogador escolheu {}'.format(item[user]))

if user == 0 and pc == 1: # jogador: pedra,  pc: papel
    print('O computador ganha.')
elif user == 1 and pc == 2: # jogador: papel , pc: tesoura
    print('O jogador ganha')
elif user == 1 and pc == 0: # jogador: papel , pc: pedra
    print('O computador ganha')
elif user == 1 and pc == 2: # jogador: papel , pc: tesoura
    print('O computador ganha')
elif user == 2 and pc == 0: # jogador: tesoura , pc: pedra
    print('O computador ganha')
elif user == 2 and pc == 1: # jogador: tesoura , pc: papel
    print('O jogador ganha')
elif user == pc: # ambos jogaram os mesmos valores
    print('Empate!')
else:
    print('COMANDO INVÁLIDO, DIGITE UM NÚMERO DE 0 A 2!')
# da vídeo aula eu só utilizei mesmo o esqueleto de pensamento, como na maioria dos outros exercícios
# prefiro esse formato de código porque é mais sucinto, limpo e objetivo
