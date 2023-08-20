print('Aluguel de carro!')
d = int(input('Digite a quantidade de dias que você utilizou o carro: '))
km = int(input('Digite quantos quilometros você percorreu com o carro: '))
vd = d * 60
vkm = km * 0.15
vt = vd + vkm
print('O {} dias utilizando o carro deu R${:.2f}.\nOs {}km rodados deu R${:.2f}.\nO total ficou R${:.2f}.'.format(d, vd, km, vkm*0.15, vt))