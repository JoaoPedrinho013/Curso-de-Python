#Exercício Python 089: Crie um programa que leia nome e duas notas
# de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.

pessoas = []
dados = []

# while True:
#
#     dados.append(str(input('Nome: ')).title())
#     dados.append(float(input('Nota 1:')))
#     dados.append(float(input('Nota 2:')))
#     pessoas.append(dados[:])
#     dados.clear()
#
#     pergunta = str(input('Quer continuar? ')).strip().upper()[0]
#     while pergunta not in 'SN':
#         pergunta = str(input('É sim ou não porra! ')).strip().upper()[0]
#     if pergunta == 'N':
#         break
# print('=-' * 30)
# print('N° NOME        MÉDIA')
# print('-' * 21)
# for indice, aluno in enumerate(pessoas):
#     print(f'{indice:<3}{aluno[0]:<12}{(aluno[1] + aluno[2]) / 2}')
# print('-' * 21)
# while True:
#     notas = int(input('Mostrar notas de qual aluno (666 kita) ? '))

#     if notas != 666:
#         print(f'Notas do {pessoas[notas][0]} são [{pessoas[notas][1]} e {pessoas[notas][2]}]')
#     else:
#         break
ficha = []
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota1:'))
    nota2 = float(input('Nota2:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    pergunta = str(input('Quer Continuar[S/N]:')).upper()[0]
    if pergunta not in 'SN':
        pergunta = str(input('Quer Continuar[S/N]:')).upper()[0]
    if pergunta == 'N':
        break
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    opcao = int(input('Mostra nota de qual aluno?(999 interrompe):'))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')