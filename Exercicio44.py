print('{:=^40}'.format(' LOJAS RAMOS '))

valor = float(input('Digite o valor do produto: R$').strip())
pag = int(input('''Digite a forma de pagamento:
[1] - À vista ou cheque
[2] - À vista no cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão
Qual opção você deseja? ''').strip())
# aqui as aspas triplas foram utilizadas pra que fosse possível pular linhas sem precisar do comando \n
if pag == 1:
    v1 = valor * 90 / 100
    print('O valor final de seu produto será R${:.2f}'.format(v1))
elif pag == 2:
    v2 = valor * 95 / 100
    print('O valor final de seu produto será R${:.2f}'.format(v2))
elif pag == 3:
    print('O valor de seu produto é R${:.2f}'.format(valor))
elif pag == 4:
    tempo = int(input('Em quantas parcelas você irá dividir?').strip())
    v3 = (valor * 0.2) + valor
    v4 = v3/tempo
    print('O valor de seu produto ao final de {} parcelas de R${:.2f} será de R${:.2f}'.format(tempo, v4, v3))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')