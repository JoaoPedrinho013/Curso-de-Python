# Exercício Python 090: Faça um programa que leia nome e
# média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

# aluno = dict()
#
# aluno['nome'] = str(input('Nome do aluno: '))
# aluno['media'] = float(input(f'Média de {aluno["nome"].title()}: '))
# print('=-' * 30)
#
# for indice, valor in aluno.items():
#     print(f'    - {indice} é igual a {valor}')
# if aluno['media'] < 5:
#     print(f'    - Situação é igual a REPROVADO!')
# if 5 <= aluno['media'] <= 7: # JEITO COMPLETO if aluno['media'] >= 5 and aluno['media'] <= 7:
#     print(f'    - Situação é igual a RECUPERÇÃO!')
# if aluno['media'] > 7:
#     print(f'    - Situação é igual a APROVADO!')
# print('=-=-=-=-=- BOA SORTE! -=-=-=-=-=')

#### PROFESSOR
aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"].title()}: '))
print('=-' * 30)
if aluno['media'] < 5:
    aluno['situação'] = 'REPROVADO'
elif 5 <= aluno['media'] <= 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'APROVADO'

for indice, valor in aluno.items():
    print(f'    - {indice} é igual a {valor}')

print('=-=-=-=-=- BOA SORTE! -=-=-=-=-=')
