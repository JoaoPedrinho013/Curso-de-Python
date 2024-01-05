#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("-="*15)
print("Analizador de triângulos")
print("-="*15)
valor1 = float(input("primeiro segmento:"))
valor2 = float(input("segundo segmento:"))
valor3 = float(input("terceiro segmento:"))
if valor1 < valor2 + valor3 and valor2 < valor1 + valor3 and valor3 < valor1 + valor3:
    print("Os segmentos acima podem formar um triangulo")
else:
    print("Os segmentos acima não podem formar um triangulo")

