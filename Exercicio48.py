# s = 0
# for c in range(0, 500): # números de 1 até 500
# 	if c % 2 == 1: # números ímpares
# 		if c % 3 == 0: # múltiplos de 3
# 			s += c # somando
# print('O somatório de todos os valores foi {}.'. format(s))
soma = 0 # acumulador vazio, soma o que encontrar
cont = 0
for c in range (1, 501, 2):
	if c % 3 == 0:
		cont += 1 # o contador soma 1 cada vez que encontra algo
		soma += c # acumulador cheio com a condição desejada
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
