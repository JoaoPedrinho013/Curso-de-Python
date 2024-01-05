# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from sympy import isprime

e = 0
n = int(input('Digite um numero:'))
for c in range(1, n + 1):
    if n % c == 0:
        e += 1
    print(c, end=' ')
print(f'\nO numero {n} foi divisível {e} vezes!')
if isprime(n):
    print(f'É PRIMO')
else:
    print(f'Não é PRIMO')

print('=' * 20)
d = 0
n = int(input('Digite um numero:'))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[92;1m ', end='')
        d += 1
    else:
        print('\033[91;1m ', end='')
    print(f'{c}', end=' ')
print(f'\033[0m\nO numero {n} foi divisível {d} vezes!')
if n == 2:
    print(f'É PRIMO')
else:
    print(f'Não é PRIMO')
