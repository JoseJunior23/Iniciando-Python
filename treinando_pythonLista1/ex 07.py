# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

i = (' !!! Calculo da Área do quadrado !!! ')
print('{:=^150}'.format(i))

base = int(input('Qual o valor da base do quadrado: '))
altura = int(input('Qual o valor da altura: '))
area = base * altura
print('O valor da area do quadrado é {} cm², e o dobro desta area é {} cm²'.format(area, area*2))