# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2º nota: '))
nota3 = float(input('Digite a 3º nota: '))
nota4 = float(input('Digite a 4ª nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4

print(' A média final do aluno foi {:.2f}.'.format(media))