import time 
inicio = time.time()


continuar = ''
pessoa = list()
lista_pessoas = list()
maior = menor = cont = 0

while True:
    pessoa.append(str(input('Digite seu nome: ').strip()))
    pessoa.append(int(input('Digite seu peso em kg: ').strip()))  # não esquecer de reverter isso lá em baixo
    lista_pessoas.append(pessoa[:])

    cont += 1
    peso = pessoa[1]
    if cont == 1:
        maior = menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso   
    pessoa.clear()

    continuar = str(input('Quer continuar? ').strip().upper())[0]
    while continuar not in 'SN':
        print('Código inválido.', end='')
        continuar = str(input('Quer continuar? [S/N]').strip().upper())[0]
    if continuar in 'N':
        break
    
print(lista_pessoas)
print(f'Foram cadastradas: {len(lista_pessoas)} pessoas')

print(f'A pessoa mais pesada tem {maior}kg e se chama ', end='')
for nome in lista_pessoas:
    if nome[1] == maior:
        nome = nome[0]
        break
print(f'{nome}')  # por conta dessa estrutura q n tava dando p imprimir mais de um nome
print(f'A pessoa mais leve tem {menor}kg e se chama ', end='')
for nome in lista_pessoas:
    if nome[1] == menor:
        nome = nome[0]
        break
print(f'{nome}')  # por conta dessa estrutura q n tava dando p imprimir mais de um nome




'''Correção:
Na resolução, são mostradas todas as pessoas com os maiores pesos, enquanto na minha solução mostra-se apenas a primeira ocorrência do maior peso.'''

'''
temp = []
principal = []
# Atenção que ao criar
#  temp = principal = [] é realizada uma conexão entre duas listas, o que não queremos
#  é necessário criar cada lista separadamente para manter a   #  independência entre elas
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:]) # isso cria uma cópia do temp que é oq queremos
    #  principal.append(temp) #  por sua vez isso cria uma ligação entre principal e temp, oq não queremos
    temp.clear()  # é necessário limpar a variavel temp pra ela n acumular os valores ao invés de gerar uma lista    # nova c os anteriores em cada input


    resp = str(input('Quer continuar? [s/n]' ))
    if resp in 'Nn':
        break
    
print('-=' * 30)
print(f'Foram cadastradas {len(principal)} pessoas')
print('-=' * 30)
print(f'O maior peso foi de {maior}kg. Peso(s) de: ', end='')

for p in principal:
    if p[1] == maior:
        print(f'{p[0]}...')
print('-=' * 30)
print(f'O menor peso foi de {menor}kg. Peso(s) de: ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}...', end='')'''

fim = time.time()
dif = fim - inicio
print(f'Tempo de execução: {dif}')