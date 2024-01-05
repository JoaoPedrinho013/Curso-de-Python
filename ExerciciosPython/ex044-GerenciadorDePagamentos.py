#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros
print('========== LOJAS XAMIS ==========')
valor = float(input('Preço da compras:R$'))
print('''FORMAS de PAGAMENTO 
[1]à vista no dinheiro/cheque 
[2]à vista no cartão 
[3]2x no cartão 
[4]3x ou mais no cartão''')
opcao = int(input('Qual é à opção?'))
if opcao == 1:
    condicao = valor-(valor*10/100)
    print(f'Sua compra de R${valor:.2f} vai custar R${condicao:.2f} no final.')
elif opcao == 2:
    condicao = valor-(valor*5/100)
    print(f'Sua compra de R${valor:.2f} vai custar R${condicao:.2f} no final.')
elif opcao == 3:
    condicao = valor/2
    print(f'Sua compra de R${valor:.2f} em 2 parcelas vai custar R${condicao:.2f} no final.')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?'))
    condicao = valor+(valor*20/100)
    valorParcelas = condicao/parcelas
    print(f'Sau compra será parcelada {parcelas}x de {valorParcelas:.2f} com juros.')
    print(f'Sua compra de R${valor:.2f} vai custar R${condicao:.2f} no final.')
else:
    print('Opção INVALIDA BURRO!!!')
