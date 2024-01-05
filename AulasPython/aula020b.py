def contador(*numeros):
    for valor in numeros:
        print(f'{valor}', end='_')
    print('FIM!')
    print(f'Recebi os valores {numeros} e são ao todo {len(numeros)} numeros!')
    print('=-' * 30)


contador(2, 3, 4, 5, 6)
contador(2, 3)
contador(2, 4, 5, 5, 6, 3, 5, 6, 4, 3, 4, 5)
