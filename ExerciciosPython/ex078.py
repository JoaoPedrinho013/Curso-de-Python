# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e
# as suas respectivas posições na lista.

numeros = list()
maior = 0
menor = 0
for cont in range(5):
    numeros.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]

print(f'Os valores da lista são {numeros}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for posicao, numero in enumerate(numeros):
    if numero == maior:
        print(f'{posicao}...', end='')
print() # ESSE E PARA PULAR UMA LINHA
print(f'O menor valor digitado foi o {menor} nas posições ', end='')
for posicao, numero in enumerate(numeros):
    if numero == menor:
        print(f'{posicao}...', end='')
print() # ESSE E PARA PULAR UMA LINHA
print('Fim')