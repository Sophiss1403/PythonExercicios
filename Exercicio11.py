largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A área da parede é: {}m² e a quantidade de tinta necessária para pintá-la é: {} litros.'.format(area, tinta))
