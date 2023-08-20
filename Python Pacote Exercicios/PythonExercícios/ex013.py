print('Vamos mostrar o valor do seu salário com acréscimo de 15%!')
s = float(input('Digite o valor do seu salário mensal:R$ '))
des = s + (s * 15/100)
print('O seu salário de R${:.2f} com o aumento de 15% fica-rá R${:.2f} .'.format(s, des))

