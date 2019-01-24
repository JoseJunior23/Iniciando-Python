# faça um programa que leia tres numeros e diga qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor:  '))
n3 = int(input('Digite o terceiro valor: '))
menor = n1
if n2 < n1 and n2 < n3:
     menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('\033[1;31;m O maior valor digitado foi {}.\033[m'.format(maior))
print('\033[1;34;m O menor valor dogotado foi {}.\033[m'.format(menor))
