'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno. A saída é feita através de uma função.'''


def texto_inicial(texto):
    print('  ' + texto)
    print('-' * (len(texto) + 4))

texto_inicial('Controle de Terrenos')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {a:.1f}m².')

area(largura, comprimento)