"""
Faça um programa que leia o ano de nascimento de um Jovem e informe,de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar.
- se já passou do tempo do alistamento.
Seu programa tambem deverá mostrar o tempo que falta ou qua passou do prazo.
"""

ano_nasc = int(input('Digite aqui o ano de seu nascimento: '))
idade = 2019 - ano_nasc
if idade < 18:
    print('\033[1;32;40mVocê ainda não tem idade para se alistar, somente daqui á {} anos.\033[m'.format(18 - idade))
elif idade == 18:
    print('\033[1;34;40mVocê vai completar 18 anos está na hora do alistamento militar:\033[m ')
else:
    print('\033[1;31;40mVocê passou da idade, seu alistamento militar deveria ter acontecido {} anos atrás.\033[m'.format(idade - 18))