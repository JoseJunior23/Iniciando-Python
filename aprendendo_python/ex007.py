# o programa deve ler duas notas de um aluno calcular e mostrar a sua media:

i = ('INICIO DO PROGRAMA')
print('{:=^200}'.format(i))

nome = input('Digite o nome do aluno:')
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1+n2)/2
print('O aluno {}, recebeu as notas {} e {}, e sua média foi de {}.'.format(nome,n1,n2,m))

f = ('FIM DO PROGRAMA')
print('{:=^200}'.format(f))
