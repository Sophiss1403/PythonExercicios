# an = a1 + (n - 1) * r
a1 = int(input('Digite o termo inicial da P.A: ').strip())
r = int(input('Digite a razão da PA: '))  # razão da PA
an = a1 + 9 * r
for c in range(a1, an + r, r):
    print('{} '.format(c), end='➡ ')
print('ACABOU')
