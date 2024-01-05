# Exercício Python 70: Crie um programa que leia o nome e
# o preço de vários produtos. O programa deverá perguntar se
# o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-' * 30)
print('LOJA DO PEDRO')
print('-' * 30)
soma = mais1000 = contador = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    contador += 1
    if contador == 1 or menorpreco > preco:
        menorpreco = preco
        menorproduto = produto
        # de vezes usar o or da pra usar esse else
    # else:
    #     if menorpreco > preco:
    #         menorpreco = preco
    #         menorproduto = produto

    continuar = ' '
    soma += preco
    while continuar not in 'SN':
        continuar = str(input('Quer continuar S/N? ')).upper().strip()[0]
    if preco >= 1000:
        mais1000 += 1
    if continuar == 'N':
        print('-----------FIM DA COMPRA-----------')
        break
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorproduto.title()} que custa R${menorpreco:.2f}')
