from math import sin, cos, tan, radians
print('Vamos mostrar o seno, cosseno e tangente do valor digitado!')
ângulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('''O seno de {0:.0f}º é {1:.2f}.
O cosseno {0:.0f}º é {2:.2f}.
A tangente de {0:.0f}º é {3:.2f}.'''.format(ângulo, seno, cosseno, tangente))


