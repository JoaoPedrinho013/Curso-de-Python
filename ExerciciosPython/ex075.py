# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# primeiro = int(input('Digite um numero: '))
# segundo = int(input('Digite outro numero: '))
# terceiro = int(input('Digite mais um numero: '))
# quarto = int(input('Digite a pergunta final: '))
#
# tupla = (primeiro, segundo, terceiro, quarto)
#
# print(f'Você digitou os valores {tupla}')
# print(f'O valor 9 apareceu {tupla.count(9)} vezes')
# if 3 in tupla:
#     print(f'O valor 3 apareceu na {tupla.index(3)+1}° posição')
# else:
#     print('O valor 3 nao foi digitado!')
# print('Os valores pares digitados foram: ', end='')
# for pares in tupla:
#     if pares % 2 == 0:
#         print(pares, end=' ')

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))

print(f'Você digitou os valores {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}° posição')
else:
    print('O valor 3 nao foi digitado!')

print('Os valores pares digitados foram: ', end='')
for pares in num:
    if pares % 2 == 0:
        print(pares, end=' ')
