print('Vamos analisar seu nome!')
nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Seu nome todo em maiúsculo: {}'.format(nome.upper()))
print('Seu nome todo em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras!'.format(dividido[0], len(dividido[0])))
