# faça umprogramaque leia um nunero de 0 á 9999 e mostrre na tela cada um dos digitos separados.
#unidade, dezena,centena,milhar

num = int(input('Digite um numero de 0 á 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 100 % 10
print('Analizando o numero temos {} ...'.format(num))
print(' Unidade: {}\n dezena: {}\n centena: {}\n milhar: {}'.format(u,d,c,m))


