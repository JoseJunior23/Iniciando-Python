""" - São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
    - São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016…
    - Não são bissextos todos os demais anos."""

# faça um programa que leia um ano qualquer,e mostre se ele é ano bissexto

i = ('  ESSE ANO É BISSEXTO  ')
print('{:¬^200}'.format(i))
from datetime import date # para pegar a data do sistema

ano = int(input('Digite um ano para saber se ele é Bissexto: '))
if ano == 0:
    ano = date.today().year # pega somente o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))

