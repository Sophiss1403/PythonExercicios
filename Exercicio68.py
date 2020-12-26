import random
par_ou_impar = ['P', 'I']
cont = 0
while True:
    sorteio = random.choice(par_ou_impar)
    usuario = str(input('Par ou ímpar? [P/I] ').upper().strip()[0])
    if usuario == sorteio:
        print('Você venceu!')
        cont += 1
    else:
        break
print(f'Você perdeu! Você ganhou {cont} vezes.')
