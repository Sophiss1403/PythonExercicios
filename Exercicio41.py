import datetime


nasc = int(input('Em que ano você nasceu? ').strip())
atual = datetime.date.year()
dif = nasc - atual
if dif <= 9:
	print('Você joga na categoria: MIRIM. ')
elif 9 < dif <= 14:
	print('Você joga na categoria: INFANTIL.')
elif 14 < dif <= 19:
	print('Você joga na categoria: JÚNIOR.')
elif 19 < dif <= 24:
	print('Você joga na categoria: SÊNIOR.')
else:
	print('Você joga na categoria: MASTER.')
