# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
i = ('\033[1;34;40m  CONVERSOR DE TEMPERATURA 1 \033[m')
print('{:§^150}'.format(i))

f = float(input('Qual a temperaura em graus Farenheit: '))
celsius = (5 * (f - 32)/ 9)
print('{} graus Farenheit, equivale á {:.2f} graus Celsius'.format(f, celsius))
