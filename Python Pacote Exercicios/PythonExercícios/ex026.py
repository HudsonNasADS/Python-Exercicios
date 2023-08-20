print('Vamos mostrar quantas lentras "A" aparece na sua frase.')
frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('Sua frase tem {} "A".'.format(frase.count('A')))
print('O primeiro aparece na posição {}'.format(frase.find('A') + 1))
print('O último "A" está na posição {}.'.format(frase.rfind('A') + 1))

