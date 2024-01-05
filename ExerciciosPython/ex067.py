#Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.
#
while True:
    contador = 0
    print('-' * 38)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 38)
    if tabuada < 0:
        break
    while contador != 10:
        contador += 1
        print(f'{tabuada} X {contador} = {tabuada * contador}')
print('PROGRAMA DE TABUADA ENCERRADO!!!')
#
# contador = 0
# multiplicador = 1
# while True:
#     print('-' * 38)
#     tabuada = int(input('Quer ver a tabuada de qual valor? '))
#     print('-' * 38)
#     if tabuada < 0:
#         break
#     for contador in range(10):
#         contador += 1
#         multiplicador = tabuada * contador
#         print(f'{tabuada} X {contador} = {multiplicador}')
# print('PROGRAMA DE TABUADA ENCERRADO!!!')
