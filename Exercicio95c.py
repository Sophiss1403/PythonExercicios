'''correção'''
time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input('Nome: ').strip())
    n_jogos = int(input('Quantidade de jogos: ').strip())
    gols.clear()
    for cont in range(n_jogos):
        gols.append(int(input(f'Gols no {cont+1}º jogo: ')))
    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    time.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N]').strip().upper())[0]
    while continuar not in 'SN':
        print('Código inválido.', end='')
        continuar = str(input('Quer continuar? [S/N]').strip().upper())[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
print('-' * 60)
print(f'{"Nº":>3}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)    
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for dado in v.values():
        print(f'{str(dado):>15}', end='')
    print()
print('-' * 60)
