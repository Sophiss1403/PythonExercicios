import datetime


nome = str(input('Olá, qual seu nome?').strip())
gen = str(input('Qual seu gênero? ').strip())
if gen == 'Feminino' or gen == 'Não binário':
    confirm = input('No seu caso, o alistamento não é obrigatório, ainda deseja continuar?').strip().upper()
    if confirm == 'SIM':
        nasc = int(input('Digite seu ano de nascimento: ').strip())
        atual = datetime.date.today()
        idade = (atual.year - nasc)
        if idade == 18:
            print('Você deve se alistar IMEDIAMENTE!')
        elif idade < 18:
            saldo = 18 - idade
            alist = nasc + 18
            print('Você deve se alistar em {} ano(s), ou seja em {}.'.format(saldo, alist))
        else:
            saldo = idade - 18
            alist = nasc + 18
            print(
                'Sua idade é {}, e você deveria ter alistado há {} ano(s), ou seja em {}. '.format(idade, saldo, alist))
    else:
        print('Tudo bem, até mais!')
else:
    print('No seu caso, o alistamento é obrigatório.')
    nasc = int(input('Digite seu ano de nascimento: ').strip())
    atual = datetime.date.today()
    idade = (atual.year - nasc)
    if idade == 18:
        print('Você deve se alistar IMEDIAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        alist = nasc + 18
        print('Você deve se alistar em {} ano(s), ou seja em {}.'.format(saldo, alist))
    else:
        saldo = idade - 18
        alist = nasc + 18
        print('Sua idade é {}, e você deveria ter alistado há {} ano(s), ou seja em {}. '.format(idade, saldo, alist))
