'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar;
 mostrando no final quantos palpites foram necessários para vencer.'''
import random
tent = 0 # fixando o valor de tentativas
pc = random.randint(0,10) # selecionando um valor qualquer em um intervalo
chute = int(input('Digite um número inteiro de 0 a 10: ')) # pedindo o chute
tent += 1 # somando uma tentativa

while chute != pc: # enquanto chute é diferente do que o pc pensou
    if chute != pc: # se o chute n é igual ao que o pc pensou
        tent +=1 # soma mais uma tentativa
        if pc > chute:
            chute = int(input('Pensei num valor maior, tente novamente: '))
        else:
            chute = int(input('Pensei num valor menor, tente novamente: '))

if tent == 1:
    print('''Você acertou de primeira! O número que você digitou foi {}, o mesmo número que o PC chutou ({}).'''.format(
        chute, pc))
elif tent > 0:
    print('''Você acertou! O número que você digitou foi {}, o mesmo número que o PC pensou ({}).
Você utilizou {} tentativa(s).'''.format(chute, pc, tent))