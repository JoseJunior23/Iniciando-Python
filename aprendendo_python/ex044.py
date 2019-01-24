"""
Elabore um programa que calcule o valor a ser pagp por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/ cheque: 10% de desconto.
- À vista no cartão: %% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

i = ('  LOJAS SEVERINO  ')
print('{:=^200}'.format(i))

valor = float(input('Digite o valor da compra: '))
print(""" FORMA DE PAGAMENTO
[1] = á vista no dinheiro/cheque
[2] - a vista no cartão
[3] - até 2x no cartão
[4] - 3 ou mais vezes no cartão """)
opcao = int(input('Qual a forma de pagamento:'))
if opcao == 1:
    print('Pagamento a vista com 10% de desconto, valor final R$ {} '.format(valor - (valor * 0.10)))
elif opcao == 2:
    print('Pagamento a vista com 5% de desconto, valor final R$ {}'.format(valor - (valor * 0.05)))
elif opcao == 3:
    print('pagamento parcelado em até 2x, valor original da compra R$ {}'.format(valor))
elif opcao == 4:
    print('Pagamento em 3 ou mais parcelas, 20% de juros, valor final R$ {}'.format(valor + (valor * 0.20)))
else:
    print('\033[1;31m OPCÃO DE PAGAMENTO INVALIDA: TENTE NOVAMENTE.\033[m')

f = ('  VOLTE SEMPRE  ')
print('{:=^200}'.format(f))