# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
n = randint(0,5) #faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
r = int(input('Em qual número:')) #O jogador tenta acertar
print('PROCESSANDO...')
sleep(2)
if r == n:
    print(f'PARABÉNS! Você conseguiu vencer!')
else:
    print(f'GANHEI! Eu pensei no número {n} e não no {r}.')
