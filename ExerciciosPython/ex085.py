# exercício Python 085: Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre
# os valores pares e ímpares em ordem crescente.


numeros = [[], []]

cont = 0
while True:
    cont += 1
    pergunta = int(input(f'Digite o {cont}° valor: '))
    if pergunta % 2 == 0:
        numeros[0].append(pergunta)
        numeros[0].sort()
    else:
        numeros[1].append(pergunta)
        numeros[1].sort()

   # OU USO A BANDEIRA if cont == 7: break
    if len(numeros[0]) + len(numeros[1]) == 7:
        break
print('=-' * 30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
