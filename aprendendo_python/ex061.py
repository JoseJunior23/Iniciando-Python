'''
Refaça o desafio 051.
Lendo o primeiro termo e a razao de uma P.A.mostrando os 10 primeiros termos da progrssão usando
'''
a = int(input('Qual é o primeiro termo da P.A: '))
r = int(input('Qual é a razão da P.A: '))
print('Os 10 primeiros termos dessa P.A é:')
termo = a
contador = 1
while contador <= 10:
    print('{},'.format(termo), end='')
    termo += r
    contador += 1
print('\nFim')