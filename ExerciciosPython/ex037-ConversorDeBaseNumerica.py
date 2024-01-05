#Escreva um programa em Python que leia um número inteiro qualquer e
#peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro:'))
print('''Escolha umas das bases de conversão:
[1]Converter para BINÁRIO
[2]Converter para OCTAL
[3]Converter para HEXADECIMAL''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('TU É BURRO, ESCREVE UM NUMERO INTEIRO PORRA')
