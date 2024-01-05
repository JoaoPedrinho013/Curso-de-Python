# Crie um programa que vai gerar cinco números aleatórios e
# colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

# numeros = ()
# maior = 0
# menor = 0
# for contador in range(0, 5):
#     numero2 = randint(1, 10)
#     numeros = numeros + (numero2,)
#
#     if contador == 0:
#         maior = numero2
#         menor = numero2
#
#     else:
#         if numero2 > maior:
#             maior = numero2
#
#         if numero2 < menor:
#             menor = numero2
# print(f'Os valores sorteados foram: {numeros}')
# print(f'O maior numero é o {maior}')
# print(f'O menor numero é o {menor}')

      ###### PROFESSOOOOOR
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor foi o {max(numeros)}')
print(f'O menor valor foi o {min(numeros)}')
