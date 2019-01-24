'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
'''
print('-='*150)
print('\033[1;34m                                                                Comercio de peixes João Papo-de-pescador\033[m')
print('-='*150)
peso = float(input('Qual a quantidade em Kg de peixes pescados hoje: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
    print('A quantidade de peixe acima do regulamento é de \033[33m{} Kg,\033[m a multa a ser paga será de \033[31m R$ {} \033[m'.format(excesso, multa))
else:
    print('\033[32m Quantidade de peixes dentro do regulamento: \033[m')

