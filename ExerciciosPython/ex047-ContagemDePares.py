# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep

print('Bora contar de 2 a 50 só os números pares')
for c in range(2, 51, 2):
    sleep(0.2)
    print(c, end=' ')
print('Acabou')
