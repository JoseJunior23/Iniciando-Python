# este  programa calcula a area de uma parede e quanto de tinta ira gastar para pinta-la sabendo que 1 litro tinta cobre 2 metros quadrados

i = ('  Tinta Para Parede  ')
print('{:¨^175}'.format(i))


c = float(input('Qual o comprimento da parede : '))
a = float(input('Qual a altura da parede : '))
area = c * a
tinta = area /2
print('A area da parede é de {:.2f}, e você usará {:.2f} litros de tinta para pinta-la.'.format(area,tinta))

f = ('  Fim do Tinta para parede  ')
print('{:¨^175}'.format(f))