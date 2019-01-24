# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

i = ('\033[1;31;40m  CONVERSOR DE TEMPERATURA 2 \033[m')
print('{:#^150}'.format(i))
c = float(input('Qual a temperatura em graus Celsius: '))
f = (c * (9/5) + 32)
print('{} graus Celsius, equivale á {:.2f} graus Farenheit'.format(c, f))