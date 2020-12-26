import random
from time import sleep

frase = 'JOGOS DA MEGA SENA'
print('-=' * 30)
print(f'{frase:^55}')
print('-=' * 30)

n = int(input('Quantos jogos serão gerados? ').strip())

frase = f' SORTEANDO {n} JOGO(S) '
print('-=' * 30)
print(frase.center(55))
print('-=' * 30)
for c,pos in enumerate(range(n)):
    c = list(random.sample(range(1, 61), 6)) 
    c.sort()

    print(f'Jogo {pos+1}: {c}')
    sleep(1)

frase = '< BOA SORTE >'
print(frase.center(60, '='))