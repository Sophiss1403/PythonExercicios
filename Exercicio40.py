prim = float(input('Digite sua nota: ').strip())
seg = float(input('Digite sua outra nota: ').strip())
media = (prim + seg) / 2
if media >= 7:
    print('Sua média foi {}. Parabéns! Você foi aprovado!'.format(media))
elif 5 <= media <= 6.9:
    print('Sua média foi {}. Você precisa e pode melhorar! Está de recuperação!'.format(media))
else:
    print('Sua média foi {}. Você está reprovado! Tente novamente no próximo ano.'.format(media))
