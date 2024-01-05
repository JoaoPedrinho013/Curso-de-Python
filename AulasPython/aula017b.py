valores = list()
valores2 = []
valores3 = list()

valores.append(1)
valores.append(2)
valores.append(3)

valores2.append(3)
valores2.append(2)
valores2.append(1)

print(valores2)

for v in valores:
    print(f'{v}...')

for v2 in valores2:
    print(f'{v2}...', end='')

print('\n')

for C, v2 in enumerate(valores2):
    print(f'Na posição {C} eu encontrei o valor {v2}')
print('Fim')

for cont in range(5):
    valores3.append(int(input('Digite um numero: ')))
for C1, v3 in enumerate(valores3):
    print(f'Na posição {C1} eu encontrei o valor {v3}!')
print('Fim 2')