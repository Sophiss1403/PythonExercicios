cbf = ('Flamengo','Santos','Palmeiras','Grêmio','Atlético Paranaense',
       'São Paulo','Internacional','Corinthians','Fortaleza',
       'Goiás','Bahia','Vasco da Gama','Atlético','Fluminense',
       'Botafogo','Ceará','Cruzeiro','Csa','Chapecoense','Avaí')
print('{:=^30}'.format('TABELA CBF'))
print(cbf)
print('{:=^30}'.format('TOP 5'))
for pos, time in enumerate(cbf[0:5]):
    print(f'Em {pos+1}º lugar: {time}')
print('{:=^30}'.format('4 ÚLTIMOS'))
for pos, time in enumerate(cbf[16:21]):
    print(f'Em {pos+17}º lugar: {time}')
print('{:=^30}'.format('Ordem alfabética'))
print(sorted(cbf))
print('{:=^30}'.format('='))
pos = cbf.index('Chapecoense')
print(f'A Chapecoense está na {pos+1}ª posição.')

