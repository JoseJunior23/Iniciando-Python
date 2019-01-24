'''
Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci
'''
i = ('\033[1;34;40m  Sequência de Fibonacci  \033[m')
print('{:=^150}'.format(i))
num = int(input('Digite a quantidade de termos você quer da sequencia :'))
anterior = 0
atual = 1
while num > 0:
    num -= 1
    print(anterior, end=', ')
    fib = atual + anterior
    anterior = atual
    atual = fib
