from random import randint
from time import sleep
print('-=-' * 25)
print('COMPUTADOR: "Vou pensar em um número de 0 a 5. Tente adivinhar o número".')
print('-=-' * 25)
jogador = int(input('Em que número eu pensei?: '))
computador = randint(0, 5)
print('PROCESSANDO...')
sleep(3.33)
if jogador == computador:
    print('''Você escolheu {} e eu pensei {}.
PARABÉNS! Você adivinhou o número!Você venceu!'''.format(jogador, computador))
else:
    print('Você escolheu {} e eu pensei {}. Eu venci!'.format(jogador, computador))