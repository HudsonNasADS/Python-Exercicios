from math import hypot
print('Vamos dar o comprimento da hipotenusa!')
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimeto do cateto adjacente: '))
hip = hypot(co, ca)
print('''O cateto oposto com comprimento {:.2f}.
E o cateto adjacente com comprimento {:.2f}.
Tem sua hipotenusa com o comprimeto {:.2f}'''.format(co, ca , hip))

