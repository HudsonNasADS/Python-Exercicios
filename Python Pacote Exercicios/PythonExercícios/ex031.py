print('Calculador de viagem.')
dist = float(input('Digite a distância da viagem que você vai fazer:km: '))
if dist <= 200:
    preço = dist * 0.5
    print('Sua viagem de {:.0f}km ficará com o preço de R${:.2f}'.format(dist, preço))
else:
    preço = dist * 0.45
    print('Sua viagem de {:.0f}km com desconto ficará com o preço de R${:.2f}'.format(dist, preço))



