#  ela é infinita e começa com 0 e 1. Os números seguintes são sempre a soma dos dois números anteriores.
termos = int(input('Digite quantos termos da sequência fibonacci deseja ver: ').strip())

a, b = 0, 1 # como é o nome dessa estrutura?
'''
a = 0
b = 1
'''
contador = 0
print('~'*55)
while contador < termos: # enquanto a qnt de num printados for menor q a qnt de num pedidos
    print(a, end=' ➡ ') # printar num
    '''c = a+b'''
    a, b = b, a+b # desloca o valor de A p/ o valor de B
    contador += 1
    '''a = b
    b = c'''
print('FIM')
print('~'*55)

'''infelizmente eu não fiz a parte importante do raciocínio do código
que era pensar o que está postulado nas linhas 4 e 9, mas eu pensei que pra que
fossem impressos os n termos seria necessário que o contador de termos fosse menor
que a quantidade de termos, aí quando chega na qnt de termos ele para'''