from random import choice
print('Sorteando um aluno para apagar o quadro!')
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
ta = [a1, a2, a3, a4]
escolhido = choice(ta)
print('O aluno escolhido para apagar o quadro foi o {}!'.format(escolhido))
