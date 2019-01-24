"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade morbida
"""

peso = float(input('Qual o seu peso atual: '))
altura = float(input('Qual a sua altura em metros: '))
Imc = (peso/ altura**2)
if Imc < 18.5:
    print('O indice se mostra {:.2f} indicam: abaixo do peso.'.format(Imc))
elif Imc >= 18.5 and Imc < 30:
    print('O indice  se mostra {:.2f} indicam: no peso ideal.'.format(Imc))
elif Imc >= 30 and Imc < 40:
    print('Indice de {:.2f} indicam: obesidade.'.format(Imc))
else:
    print('Indice de {:.2f} indicam: Obesidade Morbida')