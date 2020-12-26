''' Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares dos valores ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = list()
par = []
impar = []

for num in range(7):
    num = int(input('Número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
lista.append(par)
lista.append(impar)
par.sort()
impar.sort()
print(f'Valores pares: {lista[0]}')
print(f'Valores impares: {lista[1]}')
