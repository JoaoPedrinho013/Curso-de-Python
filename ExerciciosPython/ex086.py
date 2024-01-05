# Exercício Python 086: Crie um programa que declare uma matriz de
# dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# matriz = []
#
# for cont in range(3):
#     valor = int(input(f'Digite um valor para a posição [0, {cont+1}]: '))
#     matriz.append(valor)
# for cont in range(3):
#     valor = int(input(f'Digite um valor para a posição [1, {cont+1}]: '))
#     matriz.append(valor)
# for cont in range(3):
#     valor = int(input(f'Digite um valor para a posição [2, {cont+1}]: '))
#     matriz.append(valor)
#
# print('=-' * 30)
#
# print(f'[{matriz[0]:^5}] [{matriz[1]:^5}] [{matriz[2]:^5}]')
# print(f'[{matriz[3]:^5}] [{matriz[4]:^5}] [{matriz[5]:^5}]')
# print(f'[{matriz[6]:^5}] [{matriz[7]:^5}] [{matriz[8]:^5}]')


# PROFESSOR

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('=-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
























# matriz0 = [[], [], []]
# matriz1 = [[], [], []]
# matriz2 = [[], [], []]
# contador = 0
# while True:
#     contador += 1
#     valor = int(input('Digite um valor: '))
#     if contador == 1:
#         matriz0[0].append(valor)
#     if contador == 2:
#         matriz0[1].append(valor)
#     if contador == 3:
#         matriz0[2].append(valor)
#
#     if contador == 4:
#         matriz1[0].append(valor)
#     if contador == 5:
#         matriz1[1].append(valor)
#     if contador == 6:
#         matriz1[2].append(valor)
#
#     if contador == 7:
#         matriz2[0].append(valor)
#     if contador == 8:
#         matriz2[1].append(valor)
#     if contador == 9:
#         matriz2[2].append(valor)
#
#     if contador == 9:
#         break
# print(matriz0)
# print(matriz1)
# print(matriz2)
