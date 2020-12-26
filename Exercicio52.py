from time import sleep
num = int(input('Digite um número inteiro: '))
total = 0 # contador de divisíveis vazio
for c in range(1, num+1):
    if num % c == 0: # se e qndo o num for divisível por algum na lista do range
        print('\033[34m', end='', flush=False) # ele fica colorido
        total += 1 # contador cheio
        sleep(0.1)
    else:
        print('\033[31m', end='', flush=False) # qndo o num n é divisivel, fica vermelho
        sleep(0.2)
    print('{} '.format(c), end='', flush=False)
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, total))
if total == 2: # querendo ou não nums primos são divisíveis apenas duas vezes
    print('E, por isso, ele É PRIMO.', flush=False)
else:
    print('E, por isso, ele NÃO É PRIMO.', flush=False)
