""" O programa deve ler a velocidade de um carro, se ele ultrapassar 80kmh, receberá uma mesagen dizendo que foi mulado
a multa deve custar R$ 7.00 por cada km acima do permitido . """

i = ('  RADAR MOVEL  ')
print('{:$^200}'.format(i))

vel = float(input(' Qual a velocidade do automovel : '))
multa = (vel - 80) * 7.0
if vel > 80:
    print('\033[0;31;40m Você foi multado, por ultrapassar o limite de velocidade.')
    print('Sua multa será de {} reais \033[m'.format(multa))
print('\033[1;34;42m Diriga sempre com cuidado!!\033[m')
f = ('  FIM RADAR MOVEL  ')
print('{:$^200}'.format(f))

