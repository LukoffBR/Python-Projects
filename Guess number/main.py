from random import randint

numero_informado = -1

numero_secreto = randint(1, 100)

while numero_informado != numero_secreto:
    numero_informado = int(input('Infome o numero: '))

    if numero_informado > numero_secreto:
        print('O numero é menor')
    elif numero_informado < numero_secreto:
        print('O numero é maior')

print(f'PARABENS VOCÊ ADIVINHOU, {numero_secreto} ERA O NUMERO SECRETO!!!!!')
