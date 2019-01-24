# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
i = (' $$$ Calculo Salario $$$ ')
print('{:$^150}'.format(i))

valor_horas = float(input('Quanto você ganha por horas trabalhadas ?: '))
numero_horas = int(input('Quantas horas você trabalha no mês: '))
salario = valor_horas * numero_horas
print(' Com o total de {} horas trabalhadas no valor de R$ {}, Seu salario no final do mês será de R$:{}'.format(numero_horas, valor_horas, salario))

