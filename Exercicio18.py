from math import sin, cos, tan, radians, ceil

a = float(input('Me dê o valor de um ângulo qualquer: '))
b = sin(radians(ceil(a)))
c = cos(radians(ceil(a)))
d = tan(radians(ceil(a)))
print('O seno de {}º vale {:.1f};\nO cosseno de {}º vale {:.1f}; \nA tangente de {}º vale {:.1f} '.format(a,b, a,c, a,d))

'''print('O seno, cosseno e a tangente do ângulo {}º valem {:.1f}, {:.1f}, {:.1f}, respectivamente.' .format(a, b, c, 
d)) '''
