def soma(*valores):
    somar = 0
    for valor in valores:

        somar += valor
    print(f'Somando os valores {valores} temos {somar}')


soma(3, 4, 5, 5)
soma(5, 5, 5, 5, 5, 5, 5)
soma(4, 3, 2)
