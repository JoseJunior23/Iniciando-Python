# o programa deve ler 4 nomes e sortear uma ordem de apresentação de trabalhos
from random import shuffle
al1 = input('Nome do primeiro aluno:')
al2 = input('Nome do segundo aluno: ')
al3 = input('Nome do terceiro aluno: ')
al4 = input('Nome do quarto aluno: ')
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será : {}\n'. format(lista))