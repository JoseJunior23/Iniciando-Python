# leia o preço de um produto e mostre seu novo preço com 5% de desconto

i = ('  Calcula desconto  ')
print('{:-^175}'.format(i))

pr = float(input(' Entre com o valor do poduto : '))
des = pr * 0.05
vf = pr - des
print(' O valor inicial do produto é de ${}, com o descconto de 5% você pagará ${}.'.format(pr,vf))

f = ('  Fim do Calcula Desconto  ')
print('{:-^175}'.format(f))