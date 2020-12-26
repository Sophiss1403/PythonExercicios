def separador():
    return '-' * 30

def ficha(nome='<desconhecido>', gols=0):
    nome = input('Nome: ')
    if not nome:
        nome='<desconhecido>'
    gols = input('Gols: ')
    if not gols:
        gols = int(0)
    return f'O jogador {nome} fez {gols} gol(s).'

print(separador())
print(ficha())
print(separador())
print(ficha())
print(separador())
print(ficha())
print(separador())
print(ficha())