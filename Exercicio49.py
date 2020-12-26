num = int(input('Digite o número para que eu calcule sua tabuada: ').strip())

print('A tabuada do {} é: '.format(num))
print('-=' * 10)
for c in range(1, 11):
	print('{} x {:2} = {}'.format(num, c, num * c)) 
print('-=' * 10)