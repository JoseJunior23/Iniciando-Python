'''
Desenvolva um programa que leia o primeiro termo e a razão de uma P.A.
No final, mostre os 10 primeiros ternos dessa prograssão
'''

a = int(input('Qual é o primeiro termo da P.A: '))
r = int(input('Qual é a razão da P.A: '))
print('Os 10 primeiros termos dessa P.A é:')
for c in range(1, 11):
    pa = a+(c -1)*r
    print(pa,end=' ')