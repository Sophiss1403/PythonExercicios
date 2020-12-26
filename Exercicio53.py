# Pedir uma frase, ok
# desconsiderar seus espaços ->  ok
#
# inverter totalmente a ordem das letras** usando o índice negativo com um anterior
# verificar se a inversão é igual à frase anterior

frase = str(input('Digite uma frase qualquer: ').upper().strip())
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto.replace(' ', ''), inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')