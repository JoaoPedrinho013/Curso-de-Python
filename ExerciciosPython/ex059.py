# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
sair = 5
opcao = 0
numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
soma = numero1 + numero2
multiplicacao = numero1 * numero2

while opcao != 5:
    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa')
    opcao = int(input('Qual a sua opcao?'))

    # OPCAO 1

    if opcao == 1:
        print(f'O numero {numero1} + {numero2} é igual a {soma}')

        # OPCAO 2
    elif opcao == 2:
        print(f'O numero {numero1} x {numero2} é igual a {multiplicacao}')

        # OPCAO 3
    elif opcao == 3:
        maior = numero1
        if numero2 > numero1:
            maior = numero2
            print(f'Entre o {numero1} e o {numero2} o maior é o {maior}')
        else:
            print(f'Entre o {numero1} e o {numero2} o maior é o {maior}')
        # OPCAO 4
    elif opcao == 4:
        print('Informe os valores novamente: ')
        numero1 = int(input('Primeiro valor: '))
        numero2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando....')
    else:
        print('COMANDO INVALIDO FDP ARROMBADO!!!!')
print('FIM SEU ARROMBADO, NUNCA MAIS VOLTE!!!!')
