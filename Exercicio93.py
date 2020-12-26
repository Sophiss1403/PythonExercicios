jogador = dict()
jogador["nome"] = str(input('Nome: ').strip())
n_jogos = int(input('Quantidade de jogos: ').strip())
gols = []
for cont in range(n_jogos):
    gols.append(int(input(f'Gols no {cont+1}º jogo: ')))
jogador["gols"] = gols
jogador["total"] = sum(gols)
print('-' * 60)
print(jogador)
print('-' * 60)
for k, v in jogador.items():
    print(f' O campo {k} tem valor {v}')

print('-' * 60)
print(f'O jogador {jogador["nome"]} jogou {jogador["total"]} jogos: ')
for num, partida in enumerate(gols):
    print(f'➡ Na partida {num+1}, fez {partida} gols.')
print(f'Foi um total de {jogador["total"]} gols')