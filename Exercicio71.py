saque = int(input('Quanto você deseja sacar? R$').strip())  # pedindo o ced
total = saque
n = 0
ced = 100
divisao = total // ced
resto = total % ced

while True:  # infinitamente
    divisao = total // ced
    resto = total % ced
    n += 1
    mult = divisao * ced
    total -= mult
    if resto != 0:
        if divisao > 0:
            print(f'Total de {divisao} nota(s) de R${ced}')
        if ced == 100:
            ced = 50
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        n = 0
    elif resto < 5:
        if ced == 5:
            ced = 1
        if divisao > 0:
            print(f'Total de {divisao} nota(s) de R${ced}.')
        n = 0
        break
