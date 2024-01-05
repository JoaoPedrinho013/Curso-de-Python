#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#co = float(input('Comrpimento do cateto oposto:'))
#ca = float(input('Comprimeto do cateto adjacente:'))
#h = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A hipotenusa é {h:.2f}!')

#from math import pow, sqrt
#co = float(input('Comrpimento do cateto oposto:'))
#ca = float(input('Comprimeto do cateto adjacente:'))
#h = sqrt(pow(co, 2) + pow(ca, 2))
#print(f'A hipotenusa é {h:.2f}!')

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = hypot(co, ca)
print(f'A hipotenusa é {h:.2f}!')
