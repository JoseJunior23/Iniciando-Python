i = ('  TABUADA FACÍL  ')
print('{:=^75}'.format(i))

n = int(input('Qual numero você gostaria de saber a tabuada: '))
for c in range(0, 11):
    resultado = c * n
    print('{} x {:2} = {:2}'.format(n, c, resultado))
print('='*75)