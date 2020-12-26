# --------------------- ACUMULANDO E CONTANDO DADOS ----------------- #

cont_mulher = 0
soma_idade = 0 # acumulando idades
homem_velho = 0 # idade do homem mais velho
cont_homem = 0
nome_velho = '' # nome do homem mais velho
# ------------------ EXTRAINDO DADOS -------------------------------- #
for contador in range(1, 5):
    print("-----{}ª PESSOA-----".format(contador))
    nome = str(input('Nome:'))
    idade = int(input('Idade: '))
    soma_idade += idade  # somando idades acumuladas
    gen = int(input('''Gênero: 
[1] - Feminino
[2] - Masculino
[3] - Não binário
[4] - Outro/prefiro não informar: ''').strip())
# ------------------ DESCOBRINDO O HOMEM MAIS VELHO ------------------ # correto, só faltou o nome
    if gen == 2: # filtrando homens e contando qntos tem
        cont_homem += 1
        if cont_homem == 1: # no 1o homem, o mais velho é o 1o homem
            homem_velho = idade
            nome_velho = nome
        else: # nos demais homens
            if idade > homem_velho: # se a idade do enésimo homem for maior que a anterior
                homem_velho = idade # então o enésimo homem é o mais velho
                nome_velho = nome
# ------------------ DESCOBRINDO MULHERES MENORES DE 20 -------------- #
    if gen == 1 and idade < 20: # filtrando as mulheres com menos de 20 anos
        cont_mulher += 1 # contando-as
# ---------------------- EXIBINDO RESULTADOS ------------------------- #
print('Você indicou {} mulhere(s) com menos de 20 anos'.format(cont_mulher))
print('O homem mais velho do grupo se chama {} e tem {} anos.'.format(nome_velho, homem_velho))
print('A média de idade entre todas as pessoas do grupo é de {} anos.'.format(soma_idade/4))
