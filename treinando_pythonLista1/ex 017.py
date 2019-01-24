'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

from math import ceil
i = ('  ARCO-IRIS TINTAS  ')
print('{:/^150}'.format(i))

area = float(input('Qual o tamanho da área a ser pintada em m²: '))
quantidade_tinta = area / 6
quantidade_lata = (quantidade_tinta / 18)
quantidade_galao = (quantidade_tinta / 3.6)
# aproxima o valor das divisões para o valor mais alto
quantidade_tinta = ceil(quantidade_tinta)
quantidade_lata = ceil(quantidade_lata)
quantidade_galao = ceil(quantidade_galao)

custo1 = (quantidade_lata * 80.00)
custo2 = (quantidade_galao * 25.00)
print('=-'* 150)
print('você vai utilizar {} litros de tinta'.format(quantidade_tinta))
#menu de opções
print('''
[1] comprar apenas latas de 18 litros sendo R$ 80,00 cada uma
[2] comprar apenas galões de 3.6 litros sendo R$ 25,00 cada um
[3] misturar latas e galões onde cada lata custa  R$ 80.00 e os galões R$ 25,00 cada ''')
opcao = int(input('selecione um opção: '))
print('-='*150)
if opcao == 1:
    print('Você vai gastar {} latas de tinta, no valor final de {} reais '.format(quantidade_lata, custo1))

elif opcao == 2:
    print('Você vai gastar {} galoẽs de tinta, no valor final de {} reais '.format(quantidade_galao, custo2))

elif opcao == 3:
    misto1 = quantidade_tinta // 18 # calculo da quantidade exata de latas de tinta
    misto2 = (quantidade_tinta % 18) / 3.6 # pega o que sobrou da divisão e divide para saber quantos galões utilizar
    misto2 = ceil(misto2)
    custo3 = misto1 * 80.00
    custo4 = misto2 * 25.00
    custo_total = custo3 + custo4
    print('Você irá utilizar {} lata e {} galoẽs, no valor final de {} reais'.format(misto1, misto2, custo_total))
else:
    print('Escolha uma opção valida')
