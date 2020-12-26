'''Para escolher o formato que você deseja testar basta apagar as triplas strings.'''

'''a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjascente: '))
c = a**2 + b**2
d = c**(1/2)
print(
    'Tendo em vista o valor do cateto oposto {} e do cateto adjascente {}, a hipotenusa desse triângulo retângulo mede '
    '{}.'.format(a, b, d))'''

'''import math

a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjascente: '))
c = a ** 2 + b ** 2
print('Com o CO {} e o CA {}, o valor de HIP é {}'.format(a, b, math.sqrt(c)))'''

from math import pow

a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjascente: '))
c = a ** 2 + b ** 2
print('Com o CO {} e o CA {}, o valor de HIP é {}'.format(a, b, pow(c, 0.5)))

'''from math import sqrt

a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjascente: '))
c = a ** 2 + b ** 2
print('Com o CO {} e o CA {}, o valor de HIP é {:.1f}'.format(a, b, sqrt(c)))'''
