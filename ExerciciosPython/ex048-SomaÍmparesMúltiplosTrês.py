# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
soma2 = 0
contador = 0
contador2 = 0
print('No intervalo de 1 até 500 que são multiplos 3 é')
for n in range(0, 500, 3):
    contador += 1  # aqui ele pega todos os valores da lista e multiplica pelo valor depois do +=
    soma += n
    if n % 2 == 1:
        contador2 += 1  # O Contador contata o valor de 1 e um
        soma2 += n  # O acumulador soma ou divide os itens do loop
print(f'Soma de todos os {contador} valores é {soma}')
print(f'Soma de todos os impares {contador2} valores é {soma2}')
