'''incorreto'''
lista = list()
maior = menor = c = 0

for c in range(0, 5):
    num = int(input('Digite um número: '))
    c += 1
    if num not in lista:
        if c == 1:
            maior = menor = num
            lista.insert(-1, num)
        else:
            if num > maior:
                maior = num
                lista.insert(-1, num)
            if num < menor:
                menor = num
                lista.insert(0, num)
print(lista)
