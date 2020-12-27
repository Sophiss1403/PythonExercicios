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
    '''docstrings
    '''
    qnt = f'A quantidade de notas inseridas foi {len(args)}\n'
    maior = f'Maior nota: {max(args)}\n'
    menor = f'Menor nota: {min(args)}\n'
    s = 0
    for i in args:
        s += i
    m = s / len(args)
    media = f'Média {m}\n'
    if situ:
        if m >= 5:
            situ = 'Aprovação'
            situ = f'Situação: {situ}'
            return qnt+maior+menor+media+situ
        else:
            situ = 'Status: Reprovação'
            return qnt+maior+menor+media+situ
    else:
        return qnt+maior+menor+media


# Programa principal
print(notas(1, 2, 3, 4, situ=True))
