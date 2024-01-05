#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
altura = float(input("Digite sua altura:"))
peso = float(input("Digite sua peso:"))
imc = peso/(altura**2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc <= 24.9:
    print('Você está no peso ideal!')
elif 25 <= imc <= 29.9:
    print('Você está no sobrepeso!')
elif 30 <= imc <= 39.9:
    print('Você está com Obecidade!')
else:
    print('Você está com obecidade mórbida!')
