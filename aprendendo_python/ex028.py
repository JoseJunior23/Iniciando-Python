""" O computador deve "pensar" em um numero entre 0 e 5, o usuario deve tentar descobrir qual é esse numero
 deve escrever PARABENS se o usuario acertar ou, o computador venceu se ele não acertar."""

i = ('  INICIO DO PROGRAMA  ')
print('{:-^150}'.format(i))
# função random gera numeros aleatórios e randint para serem numeros inteiros
from random import randint
n = randint(0,5)
print(str('Vamos tentar adivinhar em qual numero o computador está "PENSANDO." '))
nUser = int(input(' Digite um numero de 0 á 5 : '))
if n == nUser:
    print('PARABENS, você é o campeão!!!, o numero escolhido pelo computador foi, {}.'.format(n,))
else:
    print('Desculpe, mas o computador venceu!!!, o numero do computador foi {}, e você escolheu o numero {}'.format(n,nUser))

f = ('  FINAL DO PROGRAMA  ')
print('{:-^150}'.format(f))