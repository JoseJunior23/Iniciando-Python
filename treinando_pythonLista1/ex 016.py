'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
from math import ceil
i = ('  AQUARELA TINTAS  ')
print('{:!^150}'.format(i))

a = float(input('Entre com a area a ser pintada em m²:'))
cobertura_tinta = a / 3
lata_tinta = cobertura_tinta / 18
lata_tinta = ceil(lata_tinta)
custo = lata_tinta * 80.00
ceil(cobertura_tinta)
print(' Será utilizado {:.2f} latas de tintas'.format(lata_tinta))
print(' O valor á ser cobrado é de {:.2f} reais '.format(custo))
