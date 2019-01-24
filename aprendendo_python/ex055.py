'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
'''
maiorP = 0
menorP = 0
for peso in range(1, 6):
    p = float(input('Qual é o peso da {}ª pessoa: '.format(peso)))
    if peso == 1:
        maiorP = p
        menorP = p
    else:
        if p > maiorP:
            maiorP = p
        if p < menorP:
            menorP = p
print('O maior peso foi {} kg '.format(maiorP))
print('O menor peso foi {} kg.'.format(menorP))