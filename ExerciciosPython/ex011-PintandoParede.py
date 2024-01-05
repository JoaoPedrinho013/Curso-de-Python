# faça um programa que leia largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro de tinta, pinta uma área de 2m ao quadrado

l = float(input('Digite a largura da parede em metros:'))
a = float(input('Digite a altura da parede em metros:'))
area = l * a
t = area/2
print(f'Será necessário {t:.2f}l litros de tinta')
