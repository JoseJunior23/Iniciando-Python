"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
-  Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/ 2
if media < 5.0:
    print('A media do aluno foi de {}, portanto o aluno está \033[1;31;40m Reprovado.\033[m'.format(media))
elif media > 5.0 and media <= 6.9:
    print('A média do aluno foi de {}, portanto o aluno está de \033[1;33;40m RECUPERAÇÃO.\033[m'.format(media))
elif media >=7.0 and media <= 10:
    print('A média do aluno foi de {}, portanto o aluno foi \033[1;34;40m APROVADO.\033[m'.format(media))
else:
    print('ERRO, VOCÊ DIGITOU UMA NOTA INVALIDA')