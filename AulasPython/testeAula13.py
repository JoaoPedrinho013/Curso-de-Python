from random import randint
from time import sleep

#Estrutura de repetição

#usando print com for
for c in range(0, 6):
    print('Oi')
print('FIM')
#######################
for c in range(0, 6):
    print('Oi')
    print('FIM 2')
#######################
for c in range(0, 6):
    print(c)
print('FIM 3')
#######################
for c in range(6, 0, -1):
    print(c)
print('FIM 4')
#######################
for c in range(20, 0, -3):
    print(c)
print('FIM 5')
#######################
for c in range(0, 20, 1):
    print(c)
print('FIM 6')
#######################
for c in range(0, 20, 2):
    print(c)
print('FIM 7')
#######################
for c in range(3):
    lista = 'pedra','papel','tesoura'
    aleatorio = randint(0,2)
    print(lista[aleatorio])
print('FIM 8')
#######################



#usando input com for
n = int(input('Digite um numero:'))
for c in range(1,n+1):
    print(c)
print('FIM9')
numero = 0
#######################
I = int(input('INICIO:'))
F = int(input('FIM:'))
P = int(input('PULA:'))
for c in range(I, F+1, P):
    print(c)
print('FIM10')
numero = 0
#######################
for c in range(3):
    n = int(input('Digite um numero:'))
print('FIM11')
#######################
s = 0
for c in range(0,5):
    n = int(input('Digite um numero:'))
    s += n
print(f'Somatorio é:{s}')

# #infinito apenas uma brincadeira
# while True:
#     print(numero)
#     sleep(0.001)
#     numero += 10
