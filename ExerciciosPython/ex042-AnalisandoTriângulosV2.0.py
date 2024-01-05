#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
valor1 = float(input("primeiro segmento:"))
valor2 = float(input("segundo segmento:"))
valor3 = float(input("terceiro segmento:"))
if valor1 < valor2 + valor3 and valor2 < valor1 + valor3 and valor3 < valor1 + valor3:
    print('Os segmentos acima podem formar um triangulo ',end='')
    if valor1 == valor2 == valor3:
        print('EQUILÁTERO!')
    elif valor1 != valor2 != valor3 != valor1:
        print('ESCALENO!')
    elif valor1 == valor2 != valor3 or valor2 == valor3 != valor1 or valor3 == valor2 != valor3:
        print('ISÓCELES!')
else:
    print('Os segmentos acima não podem formar um triangulo!')


