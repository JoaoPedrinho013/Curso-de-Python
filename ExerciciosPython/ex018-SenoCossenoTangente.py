#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
a = float(input('Digite um angulo:'))
sen = sin(radians(a))
con = cos(radians(a))
tan = tan(radians(a))
print(f'O seno é {sen:.2f}! \nO cosseno é {con:.2f}! \nA tangente é {tan:.2f}!')
