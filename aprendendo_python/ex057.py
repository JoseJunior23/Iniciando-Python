'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado peça a digitação novamente até ter um valor correto.
'''

sexo =str(input('Qual o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. digite seu sexo novamente:  ')).strip().upper()[0]
print('você cadastrou o sexo {},siga com seu cadeastro'. format(sexo))