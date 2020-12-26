print(24*'-=')
print(6*'-=',"ANALISANDO TRIÂNGULOS:" , 6*'=-')
a = float(str(input('1ª medida:')).strip())
b = float(str(input('2ª medida:')).strip())
c = float(str(input('3ª medida:')).strip())
if a < b + c and b < a + c and c < a + b:
    print('As medidas {}, {} e {} formam um triângulo.'.format(a, b, c))
else:
    print('As medidas {}, {}, e {} não formam um triângulo.'.format(a, b, c))
print(24*'=-')
