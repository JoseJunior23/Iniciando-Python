# o algoritimo deve ler um numero e mostrar o dobro o triplo e a sua raiz quadrada

n = int(input('Entre com um valor numérico: '))
d = n * 2
t = n * 3
q = n ** (1/2)
print('O numero digitado foi {}, seu dobro é {}, o seu triplo é {}, e a sua raiz quadrada é {}'.format(n,d,t,q))