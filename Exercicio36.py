print('Vamos simular o seu empréstimo para comprar sua casa!')
pcasa = float(input('Informe o valor do imóvel: R$').strip())
sal = float(input('Informe o seu salário: R$').strip())
tempo = float(input('Em quantos anos você pretende pagar? '))
meses = tempo * 12
prest = pcasa / meses
limite = sal * 30 / 100
if prest <= limite:
    desvio = (((limite - prest)/sal) * 100)
    print('Para financiar uma casa no valor de {}, em {} anos o valor das prestações a ser pago é de R${:.2f}.'
          '\nEsse valor está {:.2f}% abaixo do limite, dessa forma, seu empréstimo foi aprovado!'
          .format(pcasa, tempo, prest, desvio))
# elif prest == limite:
#     print('Para financiar uma casa no valor de {}, em {} anos o valor das prestações a ser pago é de R${:.2f}.'
#           '\nEsse valor está no limite de prestações permitido.'.format(pcasa, tempo, prest))
# essa parte do código foi desnecessária por motivos matemáticos
else:
    desvio = (((prest - limite)/sal) * 100)
    print('Para financiar uma casa no valor de {}, em {} anos o valor das prestações a ser pago é de R${:.2f}.\n'
          'Esse valor está {:.2f}% acima do limite permitido em relação ao seu salário.\n'
          'Empréstimo negado!'.format(pcasa, tempo, prest, desvio))
