"""" O programa deve ler uma frase
e mostrar quantas vezes a letra a aparece
em que posição ela aparece pela 1º vez
e emque posição aparece pela ultima vez"""

frase = str(input('Digite uma frase: ')).upper().strip()
print(' A letra A apareceu {} vezes na frase. '.format(frase.count('A')))
print('A primeira letra A esta na posição {} '.format(frase.find('A')+1))
print('A ultima letra esta na posição {} '.format(frase.rfind('A')+1))

