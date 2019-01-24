# converte reais em dolares , com a contação no  valor de 3.27:

i = ('  Conversor de Reais Para  Dolar  ')
print('{:*^150}'.format(i))

dim = float(input('Qual é o valor em Reais : '))
c = dim / 3.27
print('Você esta comprando {:2f} dolares com {}, reais '.format(c,dim))

f = ('  Fim do conversor  ')
print('{:*^150}'.format(f))
