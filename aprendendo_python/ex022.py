# criar um programa que leia o nome completo de um pessoa e mostre:

i = ('  INICIO DO PROGRAMA  ')
print('{:-^150}'.format(i))

nome = input('Digite o seu nome comleto: ').strip()
print('Analisando o seu nome temos ...')

# - o nome com todas as letras maiusculas;
print('Seu nome escrito em letras maiusculas: {}'.format(nome.upper()))

# - o nome com todas as letras minusculas;
print('Seu nome escrito com letras minusculas: {}'.format(nome.lower()))

# - Quantas letras tem sem considerar os espaços;
print('Seu nome completo tem: {} letras'.format(len(nome)- nome.count(' ')))

# - quantas letras tem o primeiro nome.
print('Seu primeiro nome tem : {} letras'.format(nome.find(' ')))

f = ('  FIM DO PROGRAMA  ')
print('{:-^150}'.format(f))


