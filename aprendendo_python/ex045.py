"""
Crie um programa que faça o computador jogar JOKENPÔ com você:
"""
from time import sleep
from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
e =(' ESCOLHA UMA DAS OPÇÕES  ')
print('{:=^175}'.format(e))
print("""
Suas opções: 
[0] Pedra 
[1] Papel 
[2] Tesoura
""")
print('='*175)
jogador = int(input('Escolha uma das opções: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('Computador jogou: {}'.format(itens[computador]))
print(('Jogador jogou: {}'.format(itens[jogador])))
if computador == 0:
    if jogador == 0:
        print('Deu empate')
    elif jogador == 1:
        print('Você Ganhou')
    elif jogador == 2:
        print('Computador Ganhou')
    else:
        print('Jogada não permitida')

elif computador == 1:
    if jogador == 0:
        print('Computador Ganhou')
    elif jogador== 1:
        print('Deu empate')
    elif jogador == 2:
        print('Você Ganhou')
    else:
        print('Jogada não permitida')

elif computador == 2:
    if jogador == 0:
        print('Você Ganhou')
    elif jogador == 1:
        print('Computador Ganhou')
    elif jogador == 2:
        print('Deu empate')
    else:
        print('Jogada não Permitida')
