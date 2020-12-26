firstnumb = int(input('Digite um número inteiro qualquer: '))
secondnumb = int(input('Digite novamente um número inteiro qualquer: '))
if firstnumb > secondnumb:
    print('O primeiro número que você digitou foi {} e ele é maior que {}.'.format(firstnumb, secondnumb))
elif firstnumb == secondnumb:
    print('Os números que você digitou têm valores iguais!')
else:
    print('O segundo número ({}) é maior que o primeiro ({}).'.format(secondnumb, firstnumb))
