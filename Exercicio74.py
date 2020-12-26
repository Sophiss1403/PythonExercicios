import random

# gerar valores aletórios e guardar eles em variáveis

numeros = tuple(random.sample(range(1,11), 5))

print(f'{numeros}')
print(f'O maior valor da sequência é: {max(numeros)}')
print(f'O menor valor da sequência é: {min(numeros)}')
