i = ('\033[1;32;40m PERCENTUAL DO SALARIO GASTO COM DESPESAS \033[m')
print('{:$^150}'.format(i))
sal = float(input('Digite o valor do salario: '))
des = float(input('Digite o valor das despezas: '))
porcentagem = (des / sal)*100
print('Você gasta {:.2f}% de seu salario com despezas.'.format(porcentagem))
