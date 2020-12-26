d = float(input('Por quantos dias você alugou esse carro? '))
km = float(input('Quantos quilômetros foram rodados nesses dias? '))
custo = 60 * d + 0.15 * km
print(f'Em função de ter rodado {km} km durante {d} dias, o valor total a ser pago é de R${custo:.2f}')
