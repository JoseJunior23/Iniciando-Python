'''
Crie um programa que leia o ano de nascimento de sete  pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maioridade = 21 anos
'''
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for contador in range(1, 8):
    data = int(input('Digite a data de nascimento da {}º pessoa: '.format(contador)))
    idade = atual - data
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('O total de pessoas maoires de idade é {}.'.format(maiores))
print('O totla de pessoas menores de idade é {}.'.format(menores))

