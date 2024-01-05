# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = list()
informacoes = []
contador = maior = menor = 0
nomeMaior = []
nomeMenor = []
while True:
    informacoes.append(str(input('Nome: ')).title())
    informacoes.append(float(input('Peso: ')))
    pessoas.append(informacoes[:])
    informacoes.clear()
    continuar = str(input('Quer continuar?')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('É sim ou não porra! ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')

for pessoa in pessoas:
    contador += 1
    if contador == 1:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
for pessoa in pessoas:
    if maior == pessoa[1]:
        nomeMaior.append(pessoa[0])
    if menor == pessoa[1]:
        nomeMenor.append(pessoa[0])

print(f'O maior peso foi {maior}kg. Peso de {nomeMaior}')
print(f'O menor peso foi {menor}kg. Peso de {nomeMenor}')

