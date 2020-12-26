import random

print('Vamos descobrir quem irá apagar a lousa para o professor hoje?')
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
lista = [a, b, c, d]
aluno = random.choice(lista)
print('O aluno que irá apagar a lousa do professor é {}.'.format(aluno))
