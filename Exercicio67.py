while True:
    num = float(input('Digite um número: ').strip())
    if num >= 0:
        for c in range(1, 11):
            resp = num * c
            print(f'{num} x {c:2} = {resp}')
            if c == 11:
                break
    else:
        print(f'Programa encerrado. Até mais!')
        break
