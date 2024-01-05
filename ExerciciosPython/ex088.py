# Exercício Python 088: Faça um programa que ajude um
# jogador da MEGA SENA a criar palpites.O programa vai
# perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#MINHA RESPOSTA
# from random import randint
# from time import sleep
# print('-' * 30)
# print(f'     JOGO DA MEGA SENA')
# print('-' * 30)
# numeros = []
#
# pergunta = int(input('Quantos jogos voce quer que eu sorteie? '))
# print(f'=-=-= SORTEANDO {pergunta} JOGOS =-=-=')
#
# for jogos in range(pergunta):
#     while True:
#         numero = randint(1, 60)
#         if numero not in numeros:
#             numeros.append(numero)
#         if len(numeros) == 6:
#             break
#     numeros.sort()
#     print(f'JOGO {jogos+1}: {numeros}')
#     numeros.clear()
#     sleep(0.3)
# print(f'=-=-=  BOA SORTE!  =-=-=')


#### CHAT GTP
# from random import sample
# from time import sleep
#
# print('-' * 30)
# print(f'     JOGO DA MEGA SENA')
# print('-' * 30)
#
# pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
# print(f'=-=-= SORTEANDO {pergunta} JOGOS =-=-=')
#
# for jogos in range(pergunta): # ESSE SAMPLE E TIPO O RANDINT POREM NAO GERA NUMERO IGUAL
#     numeros = sample(range(1, 61), 6)  # Gera 6 números únicos  E ESSE K È QUANTOS NUMEROS
#
#     print(f'JOGO {jogos+1}: {numeros}')
#     sleep(1)
#
# print(f'=-=-=  BOA SORTE!  =-=-=')

#PROFESSOR

from random import randint
from time import sleep

listas = []
jogos = list()
print('-' * 30)
print(f'     JOGO DA MEGA SENA')
print('-' * 30)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in listas:
            listas.append(num)
            contador += 1
        if contador >= 6:
            break
    listas.sort()
    jogos.append(listas[:])
    listas.clear()
    total += 1
print(f'=-=-= SORTEANDO {quantidade} JOGOS =-=-=')

for indice, lista in enumerate(jogos):
    print(f'JOGO {indice+1}: {lista}')
    sleep(0.3)
print(f'=-=-=  BOA SORTE!  =-=-=')