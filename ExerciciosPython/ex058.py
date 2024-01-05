#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from time import sleep
from random import randint
# print('Sou seu computador...')
# sleep(1)
# print('Acabei de pensar em um numero de 0 a 10.\n'
#       'Será que voce consegue advinhar qual foi?')
# sleep(0.5)
# palpite = int(input('Qual é o seu palpite? '))
# aleatorio = randint(0, 10)
#
# tentativa = 0
# while palpite != aleatorio:
#     tentativa += 1
#     if palpite > aleatorio:
#         palpite = int(input('Menos.... Tente outra vez.\n'
#                             'Qual seu palpite? '))
#     if palpite < aleatorio:
#         palpite = int(input('Mais.... Tente outra vez.\n'
#                             'Qual seu palpite? '))
# if palpite == aleatorio:
#     print(f'Acertou com {tentativa} tentativas. Parabéns shinji!')

print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um numero de 0 a 10.\n'
      'Será que voce consegue advinhar qual foi?')
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais, tente novamente')
        elif jogador > computador:
            print('Menos, tente novamente')

print(f'Acertou com {palpites} tentativas. Parabens')