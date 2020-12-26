gen = str(input('Digite o sexo [M/F/O - outro]: ')).strip().upper()
while gen not in 'MFO':
    gen = str(input('Código inválido. Digite novamente: ')).upper()
print('{} cadastrado com sucesso'.format(gen))
'''
quando eu digito f ou m de primeira ele cadastra
quando eu erro uma vez e acerto na segunda ele não interrompe a repetição
e volta a repetição

'''