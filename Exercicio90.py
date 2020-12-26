'''90. Faça um programa que leia o nome e a média de um aluno, guardando também a situação dele em um dicionário. No final mostre o conteúdo da estrutura na tela.
		-  [] Média >= 7 - aprovado
		-  [] Média < 7 - reprovado'''
nome = str(input('Nome: ').strip())
media = float(input('Média: ').strip())
if media >= 7:
    situ = 'Aprovade'
else:
    situ = 'Reprovade'

aluno = {}
aluno["nome"] = nome
aluno["media"] = media
aluno["situação"] = situ

for chave, valor in aluno.items():
    print(f'O {chave} é {valor}')
