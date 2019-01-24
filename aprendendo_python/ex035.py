print('-='*200)
print('Analisador de Triangulos')
print('-='*200)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < b + c and b < a + c and c < a + b :
    print('\033[1;34m Estes segmentos podem formar um triangulo:\033[m')
else:
    print('\033[1;33m Os segmentos NÃO podem Formar um triangulo:\033[m ')
