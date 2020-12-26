# an = a1 + (n-1) * r
a1 = int(input('Digite o termo inicial da PA: ').strip())
r = int(input('Digite a razão da PA: ').strip())
an = a1  # termo q varia, mas q começa no 1
c = 0
while c != 10:
    print('{}'.format(an), end=' ➡ ')
    c += 1
    an += r
while c == 10:
    term = int(input('Quantos mais? ').strip())
    cont = 0
    if term == 0:
        print('Fim; foram mostrados {} termos'.format(cont + 10))  # concertar isso
        break
    else:
        while cont != term:
            print('{}'.format(an), end=' ➡ ')
            an += r
            cont += 1
# o usuário digita o primeiro termo e a razão uma única vez
# da primeira vez ele mostra 10 termos
# das outras vezes ele mostra a quantidade de termos seguintes
# começando pela último termo da pa + razão
