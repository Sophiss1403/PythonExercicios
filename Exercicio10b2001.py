real = float(input('Quantos reais você quer converter? R$'))
dolar = float(input('Qual é o preço do dólar hoje? US$ '))
v = real / dolar
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, v))
