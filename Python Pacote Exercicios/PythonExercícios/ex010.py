print('Vamos mostrar a conversão do seu dinheiro para dolar!')
real = float(input('Digite o valor que você tem em reais: '))
dolar = real / 5.16
print('Você tem R${:.2f} que convertidos para dolar americano fica US${:.2f}'.format(real, dolar))