'''
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,desconsidere os espaços.
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #(split)separa as palavras em lista
junto = ''.join(palavras) #(join)junta todas as palavras sem espaço entre elas.
inverso = ''
for letra in range(len(junto)-1, -1, -1):# (len(junto -1) para pegar a ultima letra, ex 20letras ele paga do0 ao 19) vai até -1 que é antes da primeira, -1 para comecar de tras para frente.
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um Palíndromo')
else:
    print('a frse não é um Palíndromo')
