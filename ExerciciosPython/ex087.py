# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somadorPAR = somadorCOLU = maior = contador = 0
# PERGUNTA PARA COLOCAR OS NUMEROS EM ORDEM NA MATRIZ
for linha in range(0, 3):
    for coluna in range(0, 3):
        pergunta = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = pergunta
        # SOMA DE NUMEROS PARES
        if pergunta % 2 == 0:
            somadorPAR += pergunta
        # SOMA DA COLUNA 3
        if coluna == 2:
            somadorCOLU += pergunta
        # MAIOR VALOR DA LINHA 2
        if linha == 2:
            contador += 1
            if contador == 1:
                maior = matriz[1][0]
            else:
                if matriz[1][1] > maior:
                    maior = matriz[1][1]
                if matriz[1][2] > maior:
                    maior = matriz[1][2]

# MAIOR VALOR DA LINHA 2
# for numero in matriz[1]:
#     contador += 1
#     if contador == 1:
#         maior = matriz[1][0]
#     else:
#         if matriz[1][1] > maior:
#             maior = matriz[1][1]
#         if matriz[1][2] > maior:
#             maior = matriz[1][2]


print('=-' * 20)
# MOSTRAR MATRIZ
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('=-' * 20)

print(f'A soma dos valores pares é {somadorPAR}.')
print(f'A soma dos valores da terceira coluna é {somadorCOLU}.')
print(f'O maior valor da segunda linha é {maior}.')
