'''
Crie um programa que leia varios numeros inteiros pelo teclado.No final da execução.
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
'''
maior = 0
menor = 0
soma = 0
media = 0
contador = 0
saida = ' N'
while saida != 'N':
    num = int(input('Digite um valor: '))
    saida = str(input('Você quer continuar; digite [S/N]: ')).upper().strip()[0]
    contador += 1
    soma += num
    media = soma /contador
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(' Você digitou {} numeros, a soma destes é de {}, com média de {:.2f}'.format(contador, soma, media))
print(' O maior valor digitado foi {}, e o menor foi {}'.format(maior, menor))
