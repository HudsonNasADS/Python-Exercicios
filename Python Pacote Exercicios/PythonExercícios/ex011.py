print('Vamos mostrar a quantidade certa dde tinta para pintar sua parede!')
largura = float(input('Digite a largura da sua parede:(m) '))
altura = float(input('Digite a altura da dua parede:(m) '))
m2 = largura * altura
tinta = m2 / 2
print('A sua parede com {:.2f}m² precisa de {:.2f}l de tinta para pode pinta-la completamente!'.format(m2, tinta))