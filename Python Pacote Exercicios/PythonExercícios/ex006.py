print('Vamos mostrar o (d)obro, o (t)riplo e a (r)aiz quadrada do número digitado!')
n = int(input('Digite um número inteiro qualquer: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('''O número {} digitado tem o seu dobro valendo {}.
Seu triplo valendo {}.
Sua raiz quadrada valendo {:.0f}.'''.format(n, d, t, r))
