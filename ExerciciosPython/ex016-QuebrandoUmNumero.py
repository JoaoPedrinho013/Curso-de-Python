#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#Respondendo sem usar biblioteca do python
#n = float(input('Digite um numero real:'))
#print(f'O numero {n} tem como porção inteira {int(n)}')

#Usando a biblioteca math
from math import trunc
n = float(input('Digite um número real:'))
i = trunc(n)
print(f'O número real {n} tem como porção inteira {i}!')

