pessoa = {}
dados = []
mulheres = []

while True:
    pessoa.clear()
    pessoa["Nome: "] = str(input('Nome: ').strip())
    pessoa["Idade: "] = int(input('Idade: ').strip())
    pessoa["Sexo: "] = str(input('Sexo [F/M/O]: ').strip().upper())[0]

    if pessoa["Sexo: "] in 'F':
        mulheres.append(pessoa["Nome: "])
    while pessoa["Sexo: "] not in 'FMO':
        print('Código inválido.', end='')
        pessoa["Sexo: "] = str(input('Sexo [F/M/O]: ').strip().upper())[0]
        if pessoa["Sexo: "] in 'FMO':
            break

    dados.append(pessoa.copy())

    continuar = str(input('Deseja continuar? [S/N]').upper())[0]
    while continuar not in 'SN':
        print('Código inválido. ', end='')
        continuar = str(input('Deseja continuar? [S/N]').upper())[0]
    if continuar in 'N':
        break

print('-' * 30)

print(f'Pessoas cadastradas: {len(dados)}')

ids = []
for dado in dados:
    for chave, valor in dado.items():
        if chave == "Idade: ":
            ids.append(valor)
media = sum(ids) / len(ids)

print(f'Média de idade: {media}')

print(f'As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(f'{m}', end='...')
print()

print(f'Lista de pessoas com idade acima da média: ')
for dado in dados:
    for chave, valor in dado.items():
        if chave == "Idade: ":
            if valor > media:
                print(f' - {dado}')
