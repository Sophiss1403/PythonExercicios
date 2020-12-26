continuar = 'Ss'
cont_maior = cont_h = cont_m = 0
print('-' * 20)
while continuar.isalpha() is True:
    if continuar == 'Ss':
        idade = int(input('Digite a idade: '.strip()))
        sexo = input('Digite o sexo: ').upper().strip()
        print('-' * 20)
        if idade.isnumeric():
            if idade >= 18:
                cont_maior += 1
        else:
            idade = int(input('Digite a idade: '.strip()))
        # if sexo.isalphanumeric():
        #     if sexo in 'Mm':
        #         cont_h += 1
        # else:
        #     sexo = input('Digite o sexo'.strip().upper())
        # if sexo.isalphanumeric():
        #     if sexo in 'Ss':
        #         if idade < 20:
        #             cont_m += 1
