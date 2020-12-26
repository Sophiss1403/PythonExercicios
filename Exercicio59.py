from time import sleep

num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''Selecione a operação desejada:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] digitar valores novamente
    [5] sair do programa'''))

    if opcao == 1:
        resultado = num1 + num2
        print('A soma entre {:.2f} e {:.2f} é {:.2f}.'.format(num1, num2, resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print('A multiplicação entre {:.2f} e {:.2f} é {:.2f}.'.format(num1, num2, resultado))
    elif opcao == 3:
        if num1 > num2:
            print('{:.2f} é maior que {:.2f}.'.format(num1, num2))
        elif num1 == num2:
            print('{:.2f} é igual a {:.2f}.'.format(num1, num2))
        else:
            print('{:.2f} é menor que {:.2f}.'.format(num1, num2))
    elif opcao == 4:
        num1 = float(input('Primeiro valor: '))
        num2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Terminando...')
        print('=-'*25)
        sleep(3)
        print('Pronto. Volte sempre :)')

    else:
        print('Código inválido. Tente novamente:')
