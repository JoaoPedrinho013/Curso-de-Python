#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ele pode comprar ex:US$1,00=R$3,27
n = float(input("\033[1;91m"+'Digite o saldo de sua carteira:R$'))
d = n/4.99
e = n/5.47
k = n/0.0099
print("\033[1;95m"+f'Esse valor em dolar é US${d:.2f} \nEsse valor em euro é €{e:.2f} \nEsse valor em kwaza angolano é Kz{k:.2f}')
