
'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
i = ('\033[1;35;40m  CALCULANDO O PESO IDEAL HOMENS E MULHERES !!! \033[m')
print('{:*^150}'.format(i))
altura = float(input('Digite aqui a sua altura: '))
sexo = str(input('Qual o seu sexo, digite [M/F]: ')).upper().strip()[0]
if sexo == 'M':
    homens = (72.7 * altura) - 58
    print('Se você for do sexo masculino seu peso ideal seria {:.2f} Kg'.format(homens))
elif sexo == 'F':
    mulheres = (62.1 * altura) - 44.7
    print('Se você for do sexo feminino seu peso ideal seria {:.2f} Kg'.format(mulheres))
else:
    print('Erro, digite "M" para sexo masculino e "F" para sexo feminino.')
