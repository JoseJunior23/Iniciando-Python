"""
Reforço do desafio dos triangulos acrescentando o recurso de mostra que tipo de triangulo será formado:
- Equilátero: todos os lados são iguais
- Isósceles: dois laodos são iguais
- Escaleno: todos os lados são diferentes
"""

print('-='*200)
print('Analisador de Triangulos')
print('-='*200)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
condicao_existencia = a < b + c and b < a + c and c < a + b
if condicao_existencia and a == b and a == c:
    print('\033[1;34m Estes segmentos podem formar um triangulo: EQUILÁTERO\033[m')
elif condicao_existencia and a == b and a != c or a == c and c != b:
    print('\033[1;32m Estes segmentos podem formar um triangulo: ISÓSCELES\033[m')
elif condicao_existencia and a != b and a != c and b != c:
    print('\033[1;35m Estes segmentos podem formar um trinagulo: Escaleno\033[m')
else:
    print('\033[1;33m Os segmentos NÃO podem Formar um triangulo:\033[m ')