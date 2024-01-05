estados = dict()
brasil = list()

for contador in range(1, 4):
    estados['uf'] = str(input('Estado: '))
    estados['sigla'] = str(input('Sigla do Estado: ')) # ESSE FOR EU ADCIONO NO DICIONARIO E PASSO UMA COPIA
    brasil.append(estados.copy())    # PARA A LISTA
print('=-' * 20)
for estado in brasil:
    print(estado) # ESSE È UM JEITO DE PRINTAR
print('=-' * 20)
for estado1 in brasil:
    for chave, valor in estado1.items():
        print(f'O indice {chave} tem o valor {valor}! ', end='')
    print()
print('=-' * 20)
for estado2 in brasil:
    for valor2 in estado2.values():
        print(f'{valor2} ', end='')
    print()
