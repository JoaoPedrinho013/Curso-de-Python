# Quando for comecar uma tupla que é imutavel é assim () e uma lista assim [] e o dicionario {}

lanche = ('Hamburguer', 'Suco De Maracuja', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:])  ### FORMATACOES DA TUPLA
print(lanche[:2])
print(lanche[1:3])
print(lanche[-3:])
print(len(lanche))
# PARA TIRAR AS MARCACOES DA TUPLA
for cont in range(0, len(lanche)):
    print(f'Eu vou comer/tomar {lanche[cont]} na posição {cont} xDdd')

for comida in enumerate(lanche):
    print(f'Eu vou comer/tomar {comida} xDddd')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer/tomar {comida} na posição {pos} xDddddd')

for comida in lanche:
    print(f'Eu vou comer/tomar {comida} xDddddd')

print(sorted(lanche))  # coloca em ordem alfabetica

print('Comi pouco quero mais!')

### TUPLAS SAO IMUTAVEIS
# lanche[1] = 'Refrigerante' # DA ERRO
