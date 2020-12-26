from time import sleep
chamada = []
while True:
    nome = str(input('Nome: ').strip())
    nota1 = float(input('Nota 1: ').strip())
    nota2 = float(input('Nota 2: ').strip())
    media = (nota1 + nota2) / 2
    chamada.append([nome, [nota1, nota2], media])

    continuar = str(input('Quer continuar? ').strip().upper())[0]
    while continuar not in 'SN':
        print('Código inválido. ', end='')
        continuar = str(input('Quer continuar? [S/N]').strip().upper())[0]
    if continuar in 'N':
        break

print('-' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for num, dado in enumerate(chamada):
    print(f'{num:<4}{dado[0]:<10}{dado[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual alune?(999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    if opc <= len(chamada) - 1:
        print(f'Notas de {chamada[opc][0]} são {chamada[opc][1]}')
print('<<<< VOLTE SEMPRE >>>>')