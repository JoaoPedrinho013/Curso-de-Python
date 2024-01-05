# Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
#
# extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
#            'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
# numero = int(input('Digite um numero entre 0 e 20: '))
# while numero > 20 or numero < 0:
#     numero = int(input('Tente novamente. Digite um numero entre 0 e 20:'))
#
# print(f'Você digitou o número {extenso[numero]}')
#
# print('Fim')
   ### DESAFIO
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    while numero > 20 or numero < 0:
        numero = int(input('Tente novamente. Digite um numero entre 0 e 20:'))
    print(f'Você digitou o número {extenso[numero]}')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?')).upper().strip()[0]
    if continuar == 'N':
        print('-----------FIM-----------')
        break
