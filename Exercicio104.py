'''Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante à função input()
do Python, só que fazendo a validação para aceitar
apenas um valor numérico.

Ex: leiaInt(‘Digite um número inteiro’)'''


def leiaInt(entrada: str):

    while not entrada.isdecimal():
        print('EROO! Digite um número válido.')
        entrada = str(input('Digite um número: '))
    return f"Você digitou {entrada}."


# Programa principal
entrada = str(input('Digite um número: ')).strip()
print(leiaInt(entrada))
