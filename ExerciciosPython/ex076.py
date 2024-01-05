# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

# print('-' * 30)
# print('      LISTAGEM DE PREÇO')
# print('-' * 30)
# lista = (print('Lapis.................R$  1.00'),
#          print('Caneta................R$  2.00'),
#          print('Lapiseira.............R$  5.50'),
#          print('Caderno...............R$ 12.30'),
#          print('Borracha..............R$  2.60'))
# print('-' * 30)


print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)

listagem = ('Lapis', 1.50,
            'Caneta', 2.30,
            'Lapiseira', 10.45,
            'Caderno', 25.35,
            'Mochila', 323.13)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    if posicao % 2 == 1:
        print(f'R$ {listagem[posicao]:6.2f}')
print('-' * 40)