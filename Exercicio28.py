import random

pc = random.randint(0, 5)
# lembrando que no que diz ao randint é necessário colocar o intervalo, e acho que não só no randint, mas no random
# comum tbm
chute = int(input('Digite um número inteiro de 0 a 5: '))
if chute == pc:
    print('Você acertou!')
else:
    print('Você errou!')
