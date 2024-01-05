#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s = float(input('Digite seu salário R$'))
a = s+(s*15/100)
print(f'O aumento de 15% no salario é R${a:.2f}')
