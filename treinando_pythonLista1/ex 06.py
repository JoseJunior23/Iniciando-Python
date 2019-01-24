# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi
print('Vamos calcular a area de um circulo: ')
raio = int(input('Digite o valor do raio: '))
area = pi * raio **2
print('A área de um circulo de {} cm de raio, é de {:.2f} cm'.format(raio, area))