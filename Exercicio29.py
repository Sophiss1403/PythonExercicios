# primeiro eu vou fazer uma versão em que o computador diz a velocidade do carro

'''import random

vel = random.randint(0,100)

if vel > 80.00:
    y = 7*(vel - 80)
    print('Por dirigir a {}km/h, você foi multado(a) em R${:.2f}! ' .format(vel, y))
else:
    print('Continue dirigindo com segurança, na velocidade {}km/h.'.format(vel))'''

#agora vou trabalhar numa versão em que o usuário digita a velocidade do carro:

vel = float(input('Velocidade do motorista no momento: '))
if vel > 80.00:
    y = 7*(vel - 80)
    print('Por dirigir a {}km/h, você foi multado(a) em R${:.2f}!'. format(vel, y))
else:
    if vel >= 75:
        print('Continue a viagem tranquilamente!')
    else:
        print('Aumente a velocidade de seu veículo para não atrapalhar o fluxo do trânsito!')
