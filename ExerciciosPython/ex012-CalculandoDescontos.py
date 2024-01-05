#Faça um algorito que leia o preço de um produto e mostre seu novo preço,com 5% de desconto
p = float(input('Digite um preço de um produto R$'))
d = p-(p*5/100)
print(f'O valor do produto com 5% de desconto é R${d:.2f}')
