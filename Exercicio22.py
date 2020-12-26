nome = (input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())

# Nesse caso eu simplesmente fiz dessa forma, sem muitos rodeios com o código

spaces = int(nome.count(' '))
lenth = int(len(nome))
result = lenth - spaces
print(result)

"""Agora nesse caso, como eu não lembro/sei/identifiquei nenhuma função de manipulação de texto que 
me possibilite retirar os espaços do meio do texto - e com essa função eu também consigo 
retirar espaços dos extremos esquerdo e direito do texto - eu pedi pro programa encontrar e contar os espaços e 
subtrair a quantidade deles (convertendo em inteiros haha) da quantidade total da string em questão"""

div = nome.split()
print(len(div[0]))
