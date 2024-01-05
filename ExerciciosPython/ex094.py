#Exercício Python 094: Crie um programa que leia nome,
# sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D)
# Uma lista de pessoas com idade acima da média
pessoa = dict()
dados = list()
media = []
mulheres = []

while True:
    nome = pessoa['Nome'] = str(input('Nome: ')).title().strip()
    #################################################################################
    sexo = str(input('Sexo: ')).upper()
    while sexo not in "M" and sexo not in "F":
        sexo = str(input('ERRO! Por favor digite apenas M ou F: ')).upper()
    pessoa['Sexo'] = sexo
    #################################################################################
    idade = pessoa['Idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())
    media.append(idade)
    #################################################################################
    if sexo == 'F':
        mulheres.append(nome)
    #################################################################################
    continuar = str(input('Quer continuar?')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('É sim ou não porra! ')).strip().upper()[0]
    if continuar == 'N':
        break
    #################################################################################
print('=-' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'B) A média de idade é de {sum(media)/len(dados):.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for mulher in mulheres:
    print(mulher, end=', ')
print()
print(f'D) Lista de pessoas que estao acima de media: ')
for valor in dados:
    if valor['Idade'] > sum(media)/len(dados):
        print(f'    Nome = {valor["Nome"]}; Sexo = {valor["Sexo"]}; Idade = {valor["Idade"]}')
print('<< ENCERRADO! >>')
