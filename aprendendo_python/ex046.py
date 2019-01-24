"""
DESAFIO 046: Contagem Regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

"""
import emoji
from time import sleep
print('Vai comecar a contagem regressiva:')
for c in range(10, 0,-1):
    sleep(1)
    print(c)
print(emoji.emojize('\033[1;34m:collision::sparkles::collision::sparkles::collision::sparkles::collision::sparkles::collision::sparkles::collision::sparkles::collision::sparkles::collision::sparkles::collision:\033[m', use_aliases=True))
print('\033[1;31m Booom!!! Booom!!!Booom!!! \033[m')