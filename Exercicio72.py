numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
c = 0
continuar = 'Ss'
while True:
    while continuar in 'Ss':
        num = int(input('Digite um número de 0 a 20: ').strip())
        while num < 0 or num > 20:
            num = int(input('Digite um número de 0 a 20: ').strip())
        else:
            pedido = num
            for num, pos in enumerate(numeros):
                if num == pedido:
                    print(f'Você digitou o número: {pos}.')
                    c += 1
                    continuar = str(input('Quer continuar?').strip())[0]
        if c == 1:
            break
    else:
        break