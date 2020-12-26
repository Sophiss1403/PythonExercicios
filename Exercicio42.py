print("ANALISANDO TRIÂNGULOS:")
a = float(str(input('1ª medida:')).strip())
b = float(str(input('2ª medida:')).strip())
c = float(str(input('3ª medida:')).strip())
if a < b + c and b < a + c and c < a + b:
	if a == b == c:
		print('As medidas são iguais e formam um triângulo equilátero.')
	elif a == b and a != c:
		print('Existem duas medidas iguais e uma medida diferente: esse triângulo é isósceles.')
	elif a == c and a != b:
		print('Existem duas medidas iguais e uma medida diferente: esse triângulo é isósceles.')
	elif b == c and b != a:
		print('Existem duas medidas iguais e uma medida diferente: esse triângulo é isósceles.')
	elif a != b and b != c:
		print('Todas as medidas são diferentes: esse triângulo é escaleno.')
else:
	print('As medidas {}, {}, e {} não formam um triângulo.'.format(a, b, c))

