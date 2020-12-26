nintlimt = int(input('Digite um número de 0 a 9999: '))
uni = nintlimt // 1 % 10
print('unidades = {}' .format(uni))
dez = nintlimt // 10 % 10
print('dezenas  = {}' .format(dez))
cent = nintlimt // 100 % 10
print('centenas = {}' .format(cent))
mil = nintlimt // 1000 % 10
print('milhares = {}' .format(mil))
#1 é necessário fazer essa operação matemática - pelo menos com os conhecimentos de agora - pra que
#2 o número seja partido e dividido corretamente de forma que o resultado dessa operação seja justamente o
#3 algarismo correspondente à casa decimal desejada. será que fazendo essa operação com caderno, é possível
#4 alcançar esse resultado?