# Faça um programa que leia um numero qualquer e mostre o seu FATORIAL.


num = int(input('Digite um valor: '))
n = num
f = 1
print('Calculando o {}! temos:\n'.format(num), end='')
while n > 0:
    f *= n
    n -= 1
print('O fatorial do numero {} é {}'.format(num, f))
