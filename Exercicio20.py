import random

print('Vamos sortear qual será a ordem de apresentação do trabalho dessa semana!')
grupo1 = str(input('Digite o nome do primeiro grupo: '))
grupo2 = str(input('Digite o nome do segundo grupo: '))
grupo3 = str(input('Digite o nome do terceiro grupo: '))
grupo4 = str(input('Digite o nome do quarto grupo: '))

lista = [grupo1, grupo2, grupo3, grupo4]
random.shuffle(lista)

print('O grupo sorteado foi: {}'.format(lista))
