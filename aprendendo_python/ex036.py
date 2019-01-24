# escreva um programa para aprovar o emprestimo bancário para comprar uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.


i = ('\033[1;34m SIMULE AQUI SUA PRESTAÇÃO RESIDENCIAL\033[m ')
print('{:=^175}'. format(i))

valorImovel = float(input('Qual o valor do imovel pretendido: '))
salario = float(input('Qual é o valor da sua renda mensal: '))
parcelas = int(input('Em quantas parcelas será o pagamento: '))

valorParcelas = (valorImovel / parcelas)
if valorParcelas < (salario * 0.30):
    print('\033[1;36m PARABENS; seu emprestimo será aprovado, com parcelas de R$ {} mensais.\033[m'.format(valorParcelas))
else:
    print('\033[1;31m NÃO APROVADO, sua renda não é compativel: \033[m')

f =('\033[1;34m SUA SIMULAÇÃO ACABOU \033[m')
print('{:=^175}'.format(f))

