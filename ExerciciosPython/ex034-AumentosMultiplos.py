#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual o salário do funcionario?R$'))
if s <= 1250.00:
    a = s+(s*15/100)
else:
    a = s+(s*10/100)
print(f'Quem ganhava R${s:.2f} passa a ganhar R${a:.2f}!')

