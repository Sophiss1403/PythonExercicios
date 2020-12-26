palavras = 'Aprender', 'programar', 'curso', 'video', 'python', 'legal'

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} as vogais são:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')
        # if letra in 'Aa':
        #     print(f'{letra.lower()}', end=' ')
        # elif letra in 'eE':
        #     print(f'{letra.lower()}', end=' ')
        # elif letra in 'iI':
        #     print(f'{letra.lower()}', end=' ')
        # elif letra in 'oO':
        #     print(f'{letra.lower()}', end=' ')
        # elif letra in 'Uu':
        #     print(f'{letra.lower()}', end=' ')
'''No início eu pensei a resolução simples, tava dando errado, aí eu resolvi todos os problemas 
mesmo usando esse código mais difícil... vou ver o resultado e adivinha só? ele resolveu do jeito simples
que eu tinha pensado'''