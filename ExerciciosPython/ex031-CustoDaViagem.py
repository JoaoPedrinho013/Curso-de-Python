#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 parta viagens mais longas.
d = float(input('Qual a distancia da sua viagem?'))
print(f'Você esta preste a começar uma viagem de {d}Km.')
if d <= 200:
    p = d*0.50
else:
    p = d*0.45
print(f'O preço da sua passagem vai ser R${p:.2f}!')
