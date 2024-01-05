#Exercício Python 082: Crie um programa que vai ler vários números e
# colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
impar = []
par = list()

# while True:
#     num = int(input('Digite um numero: '))
#     if num % 2 == 0:
#         par.append(num)
#     else:
#         impar.append(num)
#
#     pergunta = str(input('Quer continuar?')).strip().upper()[0]
#     while pergunta not in 'SN':
#         pergunta = str(input('É sim ou não porra! ')).strip().upper()[0]
#     if pergunta == 'N':
#         break
# lista = impar + par
                            ###### PROFESSOR ######
while True:
    lista.append(int(input('Digite um numero: ')))
    pergunta = str(input('Quer continuar?')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('É sim ou não porra! ')).strip().upper()[0]
    if pergunta == 'N':
        break
for indice, vetor in enumerate(lista):
    if vetor % 2 == 0:
        par.append(vetor)
    elif vetor % 2 == 1:
        impar.append(vetor)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impar é {impar}')
