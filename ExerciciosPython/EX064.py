# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = 0
somador = 0
contador = 0
while numero != 666:
    numero = int(input('Digite um numero inteiro (666 para parar): '))
    if numero != 666:
        somador += numero
        contador += 1
print(f'Voce digitou {contador} numeros e a soma entre eles foi de {somador}.')

########## PROFESOR ###########
# cont = soma = 0
# num = int(input('Digite um valor 666 pra parar: '))
# while num != 666:
#     soma += num
#     cont += 1
#     num = int(input('Digite um valor 666 pra parar: '))
# print(f'Voce digitou {cont} numeros e a soma entre eles foi de {soma}.')
