# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

# print('-=' * 20)
# print('VAMOS JOGAR PAR OU IMPAR')
# print('-=' * 20)
# contador = 0
# while True:
#     eJogador = str(input('PAR ou IMPAR? (P/I) ')).upper().strip()
#     nJogador = int(input('Diga um valor: '))
#     print('-' * 30)
#     nComputador = randint(0, 10)
#     total = nComputador + nJogador
#     if total % 2 != 0:
#         print(f'Você jogou {nJogador} e o computador {nComputador}. Total de {total} DEU IMPAR')
#         print('-' * 30)
#         if eJogador == "P":
#             break
#     if total % 2 == 0:
#         print(f'Você jogou {nJogador} e o computador {nComputador}. Total de {total} DEU PAR')
#         print('-' * 30)
#         if eJogador == "I":
#             break
#     contador += 1
#     print('VOCÊ VENCEU!!!\n'
#           'Vamos jogar novamente...')
#     print('-=' * 20)
# print('VOCÊ PERDEU OTARIO!!!')
# print(f'GAME OVER!!! VOCE ME VENCEU {contador} vezes!!!')

#PROFESSOR
v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador {computador} o total é {total} e ele é', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce venceu!!')
            v += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    print('vamos jogar novamente')
print(f'game over. voce ganhou {v} de mim')
