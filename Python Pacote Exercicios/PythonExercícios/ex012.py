print('Vamos mostrar o desconto na sua compra!')
c = float(input('Digite o valor da sua compra:R$ '))
d = c-(c*5/100)
print('A sua compra no valor de R${:.2f} com desconto de 5% ficará R${:.2f}'.format(c, d))