def separador():
    return '-' * 30


def chamadas():
    nome = input('Nome do jogador: ')
    gols = input('Número de gols ')
    return nome, gols


def ficha():
    nome, gols = chamadas()
    if nome.isalpha():
        resp_n = f'O jogador {nome}'
        if gols.isdecimal():
            gols = int(gols)
            resp_g = f' fez {gols} gol(s).'
        return resp_n + resp_g
    else:
        return f'O jogador {nome} fez {gols} gol(s)'


print(separador())
print(ficha())
