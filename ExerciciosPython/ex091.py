#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios. Guarde esses resultados em um dicionário
# em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
# tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
# jogada = {}
# jogadores = []
#
# print('Valores sorteados: ')
#
# for contador in range(1, 5):
#     sleep(0.3)
#     jogada['nome'] = f'Jogador-{contador}'
#     jogada['numero'] = randint(1, 20)
#     print(f'{jogada["nome"]} tirou {jogada["numero"]} no dado.')
#     jogadores.append(jogada.copy())
# print('=-' * 30)
#
# print('   ===RANKING DOS JOGADORES===    ')
# jogadores.sort(key=lambda jogador: jogador['numero'], reverse=True)
#
# for cont, jogador in enumerate(jogadores):
#     print(f'{cont + 1}° lugar: {jogador["nome"]} com {jogador["numero"]}')



#### PROFESSOR


jogo = {
    'jogador-1': randint(1, 20),
    'jogador-2': randint(1, 20),
    'jogador-3': randint(1, 20),
    'jogador-4': randint(1, 20),
    'jogador-5': randint(1, 20)
    }
ranking = list()
print('Valores sorteados: ')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-' * 30)
print('   ===RANKING DOS JOGADORES===    ')
for indice, valor in enumerate(ranking):
    print(f'    {indice + 1}° lugar: {valor[0]} com {valor[1]}.')
