'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

i = ('\033[32;40m FOLHA DE PAGAMENTO \033[m')
print('{:$^150}'.format(i))

valor_hora = float(input('Qual o valor da hora trabalhada: '))
numero_hora = int(input('Qual o numero de horas trabalhadas no mês: '))
print('Descontos')
print('=-'*25)
salario_bruto = valor_hora * numero_hora
ir = (salario_bruto * 0.11)
inss = (salario_bruto * 0.08)
sindicato = (salario_bruto * 0.05)
descontos = (ir + inss + sindicato)
salario_liquido = salario_bruto - descontos
print('Descontos referente ao imposto de renda R$ = {:.2f},\nDescontos referente ao inss R$ = {:.2f},\nDescontos referentes ao sindicato R$ = {:.2f}\n'.format(ir, inss, sindicato))
print('Salario')
print('-='*25)
print('Salario deste mês livre de descontos é de R$ {:.2f}'.format(salario_liquido))
