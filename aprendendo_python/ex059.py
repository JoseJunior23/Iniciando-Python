'''
Crie um programa que leia Dois Valores e mostre um MENU :
1 - somar
2 - multiplicar
3 - maior
4 - novos numeros
5 - sair do programa
'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print(''' ESCOLHA UM OPÇÃO:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair do Programa ''')
    opcao = int(input('-> O que você deseja fazer, selecione uma opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos valores {} e {} é = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O valor da multiplicação dos numeros {},{} é = {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('\033[1;32;40m Obrigado volte sempre !!!\033[m')
    else:
        print('Opção invalida !!! Tente novamente')
    print('*'*50)






