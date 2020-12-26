frase = list(str(input('Verificarei os parêntesis: ')).strip())

abre = fecha = 0

for carac in frase:
    if '(' in carac:
        abre += 1

    if ')' in carac:
        fecha += 1

if abre == fecha:
    print('Expressão válida!')
else:
    print('Expressão inválida. Parêntesis em falta ou em excesso.')