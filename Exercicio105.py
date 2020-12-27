'''Faça um programa que tenha uma função notas() que pode
como receber várias notas de alunos e vai retornar um dicionário
como as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função'''


def notas(*args, situ=False):
    '''-> Funcao para analisar varias notas e situacao dos alunos;
    param. args: uma ou mais notas do aluno em questao
    param. situ: se True, analisa a situacao escolar do aluno, do contrario, nao o faz
    return: dicionario com as notas minima e maxima, media, situacao escolar e quantidade de notas.
    '''
    dicio = {}
    dicio['Quantidade'] = len(args)
    dicio['Maior'] = max(args)
    dicio['Menor'] = min(args)
    m = sum(args) / len(args)
    dicio['Média'] = m
    if situ:
        if m >= 5:
            dicio['Situação'] = 'Aprovação'
            return dicio
        else:
            dicio['Situação'] = 'Reprovação'
            return dicio
    return dicio


# Programa principal
print(notas(1, 2, 3, 4, situ=True))
print(notas(9.3, 2, 7, 10, 3))
print()
help(notas)
