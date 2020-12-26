from random import randint
from time import sleep

lista = []


def sorteio():
    for num in range(5):
        a = randint(0, 20)
        lista.append(a)
        print(f'Número sorteado: {a} ', flush=True)
        sleep(0.3)
def somaPar():
    soma = 0
    print(f'Soma dos números pares sorteados (', end='')
    for n in lista:
        if n % 2 == 0:
            soma += n
            print(f'{n}', end='...')
    print('):', soma)
    
# Programa principal
sorteio()
somaPar()