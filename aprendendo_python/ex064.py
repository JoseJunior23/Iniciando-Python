'''
Crie um programa que leia varios numeros inteiros pelo teclado.O programa só vai para quando o valor 999,que é a condição de parada.
no final mostre quantos numeros foram digitados e qual foi a soma entre eles
'''
soma = 0
num = 0
contador = 0
while num != 999:
    num = int(input('Digite um valor: '))
    if num != 999:
        contador += 1
        soma += num
print('Você digitou {} numeros e a somas de todos eles é de {}.'.format(contador, soma))

