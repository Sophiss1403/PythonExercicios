# an = a1 + (n-1) * r
a1 = int(input('Digite o termo inicial da PA: ').strip())
r = int(input('Digite a razão da PA: ').strip())
an = a1 # termo q varia, mas q começa no 1
c = 0 # conta qntas vezes foi impresso o a1+r
print('{}'.format(a1), end=' ➡ ') # printa o a1, ou seja n precisa mostrar mais 1/10 termos
while an != (a1+ (8*r)): # enqto an for deferente de a1 + 8 vezes a razão
    print('{}'.format(a1+r), end=' ➡ ') # printa o a1+r
    c += 1
    a1 += r # acumula no a1 esse valor q foi printado
    an = a1 + ((c-1) * r)  # acumula no an o próximo valor a ser printado
print('FIM')
