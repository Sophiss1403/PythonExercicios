# pedir um número
# o fatorial multiplica por ele mesmo menos x até multiplicar por um
# então n! = n(n-1)(n-2)(n-3) até n-x = 1
# multiplique n por n - x até que n - x = 1
# o end='' é pra ele n pular de linha NÃO ESQUECE MAIS DISSO PELO AMOR DE DEUS

num = int(input('Digite um número inteiro: ')) # pede o valor
x = num # salva ele numa variavel pq ele vai mudar lá na frente e o laço não pode parar
f = 1 # salva o elemento neutro da multiplicação
print('{}! = '.format(num), end='') # printa o número salvo, sem pular linha
while x > 0: # enquanto x for maior que 0, já que n vamos calcular fatorial negativo
    print('{}'.format(x), end='') # printa x, sem pular linha
    print(' x ' if x > 1 else ' = ', end='') # add na linha o sinal de multiplicação, poderia ser o * pra n confundir
    # como o último valor a ser printado na linha de fatorial é o 1 e depois dele tem que vir o sinal de igual
    # usamos essa estrutura de if e else pra definir oq vai ser inserido na linha
    f *= x # multiplica-se f = f * x, isto é 1 = 1* o valor que tá em x
    x -= 1 # x = x - 1 --> responsável por mostrar os números no formato "4x3x2x1" por exemplo
print('{}'.format(f)) # printa o resultado final depois de todas as rodadas de while




