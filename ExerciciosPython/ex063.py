#Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
print('SEQUENCIA DE FIBONACCI')
print('-=' * 20)
termo = int(input('Quantos termos voce quer mostrar? '))
termo1 = 0
termo2 = 1
print(f'{termo1} ➢ {termo2} ➢ ', end='')
contador = 3

while contador <= termo:
    termo3 = termo1 + termo2
    print(termo3, end=' ➢ ')
    termo1 = termo2
    termo2 = termo3
    contador += 1

print('Fim')
