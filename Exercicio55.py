# valor1 = int(input('Digite um peso em kg: ')) # pede o primeiro valor
# peso
# for comp in range(4):
#     outrovalor = int(input('Digite um peso em kg: ')) # pede outros 4 valores
#     if valor1 < outrovalor: # bagunça de variaveis
#         peso = outrovalor
#     else:
#
# print('O maior peso é: {}kg.'.format(peso))
#
# # terminar depois
maior = 0
menor = 0
for seq in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa em kg: '.format(seq)))  # pedindo 5 pesos // foi utilizado o range de 1 a 6
    # pra preencher o format com 1 até 5, entende?
    if seq == 1:  # verifica se o laço recebeu apenas 1 valor, pq com apenas um valor
        # só existe uma possibilidade de valor maior e de um valor menor.
        maior = peso  # salva o primeiro valor digitado como maior
        menor = peso  # e salva como menor tbm
    else:  # verifica se o laço recebeu mais de 1 valor
        if peso > maior:  # se o enésimo valor foi maior que o anterior
            maior = peso  # então o enésimo valor é o maior
        if peso < menor:  # se o enésimo valor for menor que o anterior
            menor = peso # então o enésimo valor é o menor
print('O maior peso digitado foi: {}kg.'.format(maior))
print('O menor peso digitado foi: {}kg.'.format(menor))
