# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from time import sleep

jogadores = []
jogador = {}
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for contador in range(partida):
        gols.append(int(input(f'Quantos gols ele fez na {contador + 1}° partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())

    while True:
        pergunta = str(input('Quer continuar?')).upper()[0]
        if pergunta in 'SN':
            break
        print('É sim ou nao porra')
    if pergunta == 'N':
        break
print('=-' * 30)
print('Cod ', end='')
for chave in jogador.keys():
    print(f'{chave:<18}', end='')
print()
for indice, valor in enumerate(jogadores):
    print(f'{indice:>3} ', end='')
    for dicionario in valor.values():
        print(f'{str(dicionario):<18}', end='')
    print()

# print(f'{"COD":<4}{"NOME":<10}{"GOLS":>10}{"TOTAL":>30}')
# print('-' * 60)
# for cont, valor in enumerate(jogadores):
#     print(f'{cont:<4}{valor["nome"]:<15}{str(valor["gols"]):^10}{valor["total"]:>25}')

while True:
    opcao = int(input('Mostrar dados de qual jogador?(69 interrompe):'))
    if opcao > len(jogadores):
        print(f'ERRO. Não existe jogador com o codigo {opcao}!')

    if opcao <= len(jogadores) - 1:
        print(f'--LEVANTAMENTO DO JOGADOR {jogadores[opcao]["nome"]}:')
        for cont1, valor in enumerate(jogadores[opcao]["gols"]):
            print(f'No jogo {cont1 + 1} fez {valor}')
            sleep(0.3)

    if opcao == 69:
        print('FINALIZANDO...')
        break
