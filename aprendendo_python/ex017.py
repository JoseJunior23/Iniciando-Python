# ler o comprimento dos catetos de um tringula retangulo, e calcular o comprimento da hipotenusa.
import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print('O valor da hipotenusa é de {:.2f}.'.format(h))
