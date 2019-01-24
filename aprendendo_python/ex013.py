# leia o salario de um funcionario e mostre seu novo salario com  15% de aumento

i = (' Aumento Salario ')
print('{:$^175}'.format(i))

nome = input('Entre com o nome do funcionário: ')
sal =  float(input('Qual o valor do salario : '))
a = sal * 0.15
nsal = sal + a
print('O funcionário {}, com o salario de {}, receberá um novo salario de {} referente ao aumento de 15%'.format(nome,sal,nsal))

f = ('  Fim do Aumento Salario  ')
print('{:$^175}'.format(f))