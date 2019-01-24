# ler um angulo qualquer e calcular o seu seno cosseno e a tangente
import math
i = ('  INICIO DO PROGRAMA  ')
print('{:-^150}'.format(i))

an = float(input('Digite o valor de um angulo: '))
seno = math.sin(math.radians(an))
print(' O valor do seno do ângulo {} é de {:.2f}.'.format(an, seno))
cos = math.cos(math.radians(an))
print(' O valor do cosseno do ângulo {} é de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print(' A tangente do ângulo {} é de {:.2f}.'.format(an, tan))

f = ('  FIM DO PROGRAMA  ')
print('{:-^150}'.format(f))