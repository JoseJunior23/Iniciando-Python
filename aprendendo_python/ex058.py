
'''
DESAFIO 058: Jogo da Adivinhação v2.0

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
'''

from random import randint
n = randint(0, 10)
print('Tente advinhar o numero escolhido pelo sistema:')
print('O numero escolhido foi de 0 á 10.')
certo = False
tentativa = 0
while not certo:
    nuser = int(input('Então escolha um valor entre 0 e 10: '))
    tentativa += 1
    if nuser == n:
        certo = True
    else:
        print('Você errou, tente novamente !!!')
print('O número escolhodo pelo computador foi {} e você escolheu {}:Parabens você ACERTOU !!!'.format(n, nuser))
print('Você tentou {} vezes até acertar o numero correto'.format(tentativa))


