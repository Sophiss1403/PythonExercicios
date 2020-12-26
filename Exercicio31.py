dist = float(input('Qual é a distância da sua origem até seu destino? '))
if dist <= 200:
	y = dist*0.5
	print('O valor de sua passagem é R${}. '. format(y))
else:
	x = dist*0.45
	print('O valor de sua passagem é {}'. format(x))