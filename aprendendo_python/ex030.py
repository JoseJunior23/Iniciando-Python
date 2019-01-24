# criar um programa que mostra se um numero é PAR ou IMPAR :

num = int(input('Digite um numero para saber se ele é PAR ou IMPAR: '))
n = (num % 2)
if n == 0:
    print('O numero {}  é PAR: '.format(num))
else:
    print('O numero {} é IMPAR: '.format(num))
