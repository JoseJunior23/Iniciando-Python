"""
Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
1 para binario
2 para octal
3 para hexadecimal
"""

i = ('\033[1;35;40m  CONVERSOR NUMÉRICO  \033[m')
print('{:*^200}'.format(i))

n = int(input('Digite um numero cara conversão: '))
print(''' Escolha uma das bases para fazer a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Qual a sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido na base OCTAL é {} .'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(n, hex(n)[2:]))
else:
    print('\33[1;31m OPÇÃO INVALIDA, opções são de 1 á 3: \033[m')
