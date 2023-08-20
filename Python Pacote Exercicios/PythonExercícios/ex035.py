print('Vamos mostra se as retas formam um triâgulo.')
print('='*25)
print('ANALISADOR DE TRIÂNGULOS')
print('='*25)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triâgulo!')
else:
    print('Os segmentos acima nãp podem formar um triângulo.')

