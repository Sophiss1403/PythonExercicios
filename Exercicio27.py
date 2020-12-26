nome = str(input('Digite o seu nome completo: ')).strip()
resp1 = nome.split()
resp2 = nome.rsplit()
print('Olá, {} {}!'.format(resp1[0], resp2[-1]))
