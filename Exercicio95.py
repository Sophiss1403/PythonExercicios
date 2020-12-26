jogador = dict()
time = []
gols = []
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
print(f'{"Nº":>3}{"Nome":>15}{"Gols":>15}{"Total":>15}')
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for dado in v.values():
        print(f'{str(dado):>15}', end='')
    print()

while True:
    print('-' * 60)
    opc = int(input('Visualizar detalhes de qual jogador? (999 interrompe) ').strip())
    if opc == 999:
        break
    while opc > len(time):
        print('Código inválido.', end='')
        opc = int(input(f"Digite um número entre 0 e {len(time) - 1} para seguir: ").strip())
    if opc <= len(time) - 1:
        print()
        print(f'Dados de {time[opc]["nome"]}: ')
        for num, partida in enumerate(time[opc]["gols"]):
            print(f' ➡ Na partida {num+1}, fez {[partida]} gol(s).')
        print()
        print(f'Foi um total de {time[opc]["total"]} gols')
