"""
A confedaração nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- até 09 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 16 anos: JUNIOR
- Até 20 anos: ADULTO
- Acima: MASTER
"""

ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = 2019 - ano_nasc
if idade <= 9:
    print('O atleta tem {} anos, se encaixa na categoria: MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print(' O atleta tem {} anos, se encaixa na categoria: INFANTIL'.format(idade))
elif idade > 14 and idade <= 16:
    print('O atleta tem {} anos, se encaixa na categoria: JUNIOR'.format(idade))
elif idade > 16 and idade <= 20:
    print('O atleta tem {} anos, se encaixa na categoria: ADULTO'.format(idade))
else:
    print('O atleta tem {} anos, se encaixa na categoria: MASTER'.format(idade))
