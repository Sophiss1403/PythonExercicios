continuar = 'Ss'
cont_maiores = cont_homens = cont_mulheres = 0
print('-'*20)
while continuar in 'Ss':
    idade = int(input('Qual a sua idade? ').strip())
    sexo = str(input('Qual seu gênero? [M/F/O/NB] ').strip().upper()[0:1])
    print('-' * 20)
    continuar = str(input('Deseja continuar? [S/N]').strip().upper()[0])
    print('-' * 20)
    if idade > 18:
        cont_maiores += 1
    if sexo in 'Mm':
        cont_homens += 1
    if sexo in 'Ff':
        if idade < 20:
            cont_mulheres += 1
print(f'''Maiores de 18: {cont_maiores}
Homens: {cont_homens}
Mulheres com menos de 20 anos: {cont_mulheres}.''')
# continuar = 'Ss'
# cont_maiores = cont_homens = cont_mulheres = 0
# print('-'*20)
# while continuar not in 'Nn':
#     idade = input('Digite a idade: ')
#     while not idade.isdigit():
#         idade = input('Digite novamente a idade: ')
#     if int(idade) >= 18:
#         cont_maiores += 1
#     gen = input('Digite o gênero: [F/M/NB/O]').strip().upper()[0:1]
#     while gen is not 'MmFfOoNBnb':
#         gen = input('Digite novamente o gênero: [F/M/NB/O]').strip().upper()[0:1]
#     if gen in 'Mm':
#         cont_homens += 1
#     if gen in 'Ff':
#         if int(idade) <= 20:
#             cont_mulheres += 1
#     continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
#     while not continuar.isalpha():
#         continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
#     if continuar in 'Nn':
#         break
# print(f'''Pessoas com mais de 18: {cont_maiores}.
# Homens cadastrados: {cont_homens}.
# Mulheres com menos de 20: {cont_mulheres}.''')
