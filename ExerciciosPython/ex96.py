#  Faça um programa que tenha uma função chamada área(), que receba as
#  dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(a, b):
    print(f'A área de um terreno de {a}x{b} é de {a * b:.1f}m²')


print('CONTROLE DE TERRENOS')
print('-=' * 15)
# a = float(input('Largura: '))
# b = float(input('Comprimento: '))
# area(a, b)
area(a=float(input('Largura: ')), b=float(input('Comprimento: ')))
