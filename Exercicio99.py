from time import sleep


def maior(*args):
    print('-=' * 30)
    print('Analisando os valores passados...', flush=True)
    sleep(0.5)
    print('Valor(es) informado(s): ', end='')
    for num in args:
        print(num, end=' ')
    
    if len(args) == 0:
        print('0') 
        print(f'Foram informados {len(args)} valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        print()
        print(f'Foram informados {len(args)} valores ao todo.')
        print(f'O maior valor informado foi {max(args)}')
# Programa principal
maior(1, 2)
maior(2, 9, 4, 5, 7, 1)
maior(6)
maior(4, 7, 0)
maior()