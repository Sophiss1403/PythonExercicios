n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
# Verificando o menor valor:
menor = n3 
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
# Verificando o maior valor:
maior = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))