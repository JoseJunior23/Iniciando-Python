
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

i = ('\033[1;33;47m  CALCULANDO O PESO IDEAL GENÉRICO !!! \033[m')
print('{:+^150}'.format(i))

altura = float(input(' Qual é a sua altura: '))
peso_ideal = (72.7 * altura) - 58
print('Com {} m de altura seu peso ideal seria {:.2f} Kg'.format(altura, peso_ideal))