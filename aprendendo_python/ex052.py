'''
Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
'''
tot = 0
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\033[m\nO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print(' Por isso ele é PRIMO')
else:
    print( 'Por isso ele NÃO é PRIMO')