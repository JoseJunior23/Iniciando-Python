# ler um numero real e mostrar somente sua parte inteira
from math import trunc,ceil
num = float(input('Digite um numero real: '))
print('a parte inteira do {} é {}.'.format(num,trunc(num)))