num = int(input('Digite um número: '))
x = num
f = 1
print('{}! ='.format(x), end=' ')
for x in range(x, 0, -1):
    print(x, end='')
    print(' *' if x > 1 else ' = ' , end=' ')
    f *= x
    x -= 1
print('{}'.format(f), end='')
