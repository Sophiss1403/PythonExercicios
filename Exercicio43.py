print('Vamos calcular seu IMC? ')

peso = float(input('Digite seu peso em kg: ').strip())
altura = float(input('Digite sua altura em metros: ').strip())
imc = float(peso / altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f}, e você está abaixo do peso. Procure um nutricionista. '.format(imc))
    p2 = (peso / 25) * imc
    delta_peso = peso - p2
    print('É necessário que você engorde {:.2f} kg'.format(delta_peso))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.2f}, e você está no peso ideal.'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f}, e você está em sobrepeso. Procure fazer exercícios!'.format(imc))
    p2 = (peso / 25) * imc
    delta_peso = p2 - peso
    print('É necessário que você emagreça {:.2f} kg.'.format(delta_peso))
elif 30 < imc <= 40:
    p2 = (peso / 25) * imc
    delta_peso = p2 - peso
    print('Seu IMC é {:.2f}, e você está com obesidade. Procure um especialista.'.format(imc))
    print('É necessário que você emagreça {:.2f} kg.'.format(delta_peso))
elif imc >= 40:
    print('Seu IMC é {:.2f}, e você está com obesidade mórbida. Procure um médico!'.format(imc))
    p2 = (peso / 25) * 40
    delta_peso = p2 - peso
    print('É necessário que você emagreça {:.2f} kg.'.format(delta_peso))
