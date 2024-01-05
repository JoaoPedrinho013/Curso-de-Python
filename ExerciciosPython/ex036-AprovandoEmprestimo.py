#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Valor da Casa:R$"))
salario = float(input("Qua o salário do comprador:R$"))
anos = int(input("Quantos anos de financiamento?"))
finaciamentoMensal = anos * 12
parcelas = valorCasa / finaciamentoMensal
porcentagemDoSalario = salario*30/100

print(f"Para pagar a casa de R${valorCasa:.2f} em {anos}anos a prestação será {parcelas:.2f}!")
if parcelas > porcentagemDoSalario:
    print("Seu financiamento foi negado!")
else:
    print(f"Seu financiamento foi aceito!")
