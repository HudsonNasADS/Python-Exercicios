print('Vamos mostrar as informações do dado digitado!')
n = input('Digite algum dado qualquer: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('O dado digitado é numérico? {}'.format(n.isnumeric()))
print('O dado digitado é alfanumérico? {}'.format(n.isalnum()))
print('O dado digitado é maiúsculo? {}'.format(n.isupper()))
print('O dado digitado é minúsculo? {}'.format(n.islower()))
print('O dado digitado tem só espaços? {}'.format(n.isspace()))

