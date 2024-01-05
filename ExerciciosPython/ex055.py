# Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.
maiorPeso = float(input('Peso da 1ª Pessoa: '))
menorPeso = maiorPeso
for pessoas in range(2, 6):
    peso = float(input(f'Peso da {pessoas}ª pessoa:'))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
         menorPeso = peso
print(f'O maior peso lido foi de {maiorPeso}Kg\n'
      f'O menor peso lido foi de {menorPeso}Kg')
