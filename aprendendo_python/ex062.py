primeiro_termo = int(input('Qual é o primeior termo da P.A: '))
razao = int(input('Qual é a razão da P.A: '))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{},'.format(termo),end='')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Foi mostrado {} termos desta P.A'.format(total))