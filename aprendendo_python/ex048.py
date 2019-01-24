"""
DESAFIO 048: Soma Ímpares Múltiplos de Três

Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.

"""
soma = 0
for c in range(1, 500 +1, 2):
    if c % 3 == 0:
       print(c, end=' ')
       soma += c
print('\n A soma deste numeros é de {}'.format(soma))

