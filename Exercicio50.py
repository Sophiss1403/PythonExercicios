s = 0
for c in range(0,6):
	num = int(input('Digite o número:  ')) # perguntando 6 valores
	if num % 2 == 0: # selecionando os pares
		s += num # somando os valores selecionados (pares)
print('O somatório de todos os valores pares foi {}.'.format(s))
