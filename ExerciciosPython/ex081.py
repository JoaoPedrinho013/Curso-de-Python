#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    pergunta = str(input('Quer continuar?')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('É sim ou não porra! ')).strip().upper()[0]
    if pergunta == 'N':
        break

print(f'Você digitou {len(numeros)} elementos!')

numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')

if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao faz parte da lista!')
