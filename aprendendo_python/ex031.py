"""" O programa deve perguntar a distancia de uma viagem ao usuario,e
calcular o valor da passagem, cobrando R$ 0,50 por km para viagens até 200 km
e R$ 0.45 para viagens mais longas."""

i = ('  VALOR DA PASSAGEM  ')
print('{:!^200}'.format(i))

distancia = float(input('Qual será a distância da sua viagem: '))
print(' Calculando o valor da viagem!!! ')
if distancia <= 200:
    valor1 = (distancia * 0.50)
    print('O valor da sua passagem será de {} reais. '.format(valor1))
else:
    valor2 = (distancia * 0.45)
    print('O valor da sua passagem será de {} reais. '.format(valor2))

f = ('  FIM  ')
print('{:!^200}'.format(f))