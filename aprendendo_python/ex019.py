# um professor vai sortear entre 4 alunos quem vai apagar o quadro, fazer um programa que leia o nome dos alunos e faça o sorteio.
import random
al1 = str(input('Qual o nome do primeiro aluno: '))
al2 = str(input('Qual o nome do segundo aluno: '))
al3 = str(input('Qual onome do terceiro aluno: '))
al4 = str(input('Qual o nome do quarto aluno: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('O aluno escolhido para apagar a lousa foi {}.'.format(escolhido))

