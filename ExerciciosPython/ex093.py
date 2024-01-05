#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = {
    'Nome': str(input('Nome do jogador: ')).title().strip(),
    'Gols': 0,
    'Total': 0
}
gols = []
totalGols = cont = 0
partida = int(input('Quantas partidas ele jogou? '))
#################################################################################
for contador in range(partida):
    gols.append(int(input(f'Quantos gols ele fez na {contador+1}° partida? ')))
    dados['Gols'] = gols
#################################################################################
# dados['Total'] = sum(gols) Esse parametro sum soma tudo que ta nos () no caso ali é uma lista
for valor in gols:
    totalGols += valor
dados['Total'] = totalGols
#################################################################################
print('=-' * 30)
print(dados)
print('=-' * 30)
#################################################################################
for key, value in dados.items():
    print(f'O campo -{key} tem o valor: {value}')
#################################################################################
print('=-' * 30)
print(f'O jogador {dados["Nome"]} jogou {partida} partidas!')
for val in gols:
    cont += 1
    print(f'    => Na partida {cont}, ele fez {val} gols.')
print(f'Foi um total de {totalGols} gols.')
### PROFESSOR ULTIMO PRINT SO
# for i, v in enumerate(dados['Gols']):
#     print(f"   -'- Na partida {i+1}, ele fez {v} gols.")