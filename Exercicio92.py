from datetime import date
dados = dict()

dados["Nome: "] = str(input('Nome: ').strip())
nasc = int(input('Ano de nascimento: ').strip())
dados["CTPS: "] = int(input('Nº da carteira da trabalho (0 se não tiver): ').strip())

atual = date.today().year
dados['Idade: '] = atual - nasc


if dados["CTPS: "] != 0:
    dados["Contrato: "] = int(input('Ano de contratação: ').strip())
    dados["Salário: R$"] = int(input('Salário R$ ').strip())
else:
    for k, v in dados.items():
        print(f'{k} {v}.')

dados['Aposenta aos'] = (dados['Idade: '] + 35) - (atual - dados["Contrato: "])
print('-' * 30)
for k, v in dados.items():
        print(f' - {k} {v}.')
