print('CALCULO DE MULTA.')
velocidade = int(input('Digite a velocidade que estava.km/h: '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('''Sua velocidade é de {}km/h.
Você está dentro da velocidade permitida. Siga sua viagem!'''.format(velocidade))
else:
    print('''MULTADO!
Sua velocidade é de {}km/h. 
Você ultrapassou em {}km/h o limite de velocidade.
Sua multa foi de R${:.2f}'''.format(velocidade, velocidade - 80,multa))