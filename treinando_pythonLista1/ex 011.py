'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
print('=-'*150)
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = float(input('Terceiro numero: '))
equacao1 = ((n1 * 2) * (n2 / 2))
equacao2 = ((n1 * 3) + n3)
equacao3 = (n3 ** 3)
print('=-'*150)
print('O produto do primeiro com metade do segundo é = {}'.format(equacao1))
print('A soma do triplo do primeiro com o terceiro é = {}'.format(equacao2))
print('O terceiro elevado ao cubo é = {}'.format(equacao3))
print('=-'*150)
