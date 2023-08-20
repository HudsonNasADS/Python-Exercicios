print('Vamos mostrar o menor e o maior número.')
a = int(input('Digite o preimeiro valor: '))
b = int(input('Digte o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número digitado foi o {}!'.format(menor))
print('O maior número digitado foi o {}! '.format(maior))
        