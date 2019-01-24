# escreva um programa que leia o salario, e calcule 15% de aumento para salarios menores de R$ 1250.00, e 10% para salarios acima desse valor

salario = float(input('Digite o valor do salario do funcionário: '))
newsalario1 = (salario * 0.15) + salario
newsalario2 = (salario * 0.10) + salario
if salario < 1250.00:
    print('Seu novo salario é de {} reais'.format(newsalario1))
else:
    print('Seu novo salario é de {} reais '.format(newsalario2))