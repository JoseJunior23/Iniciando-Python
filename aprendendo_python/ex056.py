'''
Desenvolva um  programa que leia o nome a idade e sexo de 4 pessoas. No final do programa, mostre.
A media de idade do grupo.
Qual o nome do homen mais velho
Quantas mulheres tem menos de 20 anos
'''


maiorIdadeHomen = 0
nomeVelho = ''
totalMulher = 0
media = 0
for pessoas in range(1, 5):
    print('================= {}ª PESSOA   ================'.format(pessoas))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo [M/F] : ')).strip()
    media += idade
    if pessoas == 1 and sexo in 'Mm':
        maiorIdadeHomen = idade
        nomeVelho = nome
    if sexo in 'Mm'and idade > maiorIdadeHomen:
        maiorIdadeHomen = idade
        nomeVelho = nome
    if sexo in 'Ff'and idade < 20:
            totalMulher += 1
print('A media das idades é {}'.format(media/4))
print('O homen mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomen, nomeVelho))
print('O total de mulheres com menos de 20 anos é {}.'.format(totalMulher))