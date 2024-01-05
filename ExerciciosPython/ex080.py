# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

# valores = []
#
# for cont in range(5):
#     valor = int(input('Digite um valor: '))
#     if cont == 0:
#         valores.insert(0, valor)
#         print(f'O valor {valor} foi adicionado ao final da lista...')
#
#     if cont == 1:
#         if valor > valores[0]:
#             valores.insert(1, valor)
#             print(f'O valor {valor} foi adcionado ao final da lista')
#         else:
#             valores.insert(0, valor)
#             print(f'O valor {valor} foi adicionado na posicao 0')
#
#     if cont == 2:
#         if valor > valores[1]:
#             valores.insert(2, valor)
#             print(f'O valor {valor} foi adcionado ao final da lista')
#
#         if valor >= valores[0] and valor <= valores[1]:
#             valores.insert(1, valor)
#             print(f'O valor {valor} foi adicionado na posicao 1')
#
#         if valor < valores[0]:
#             valores.insert(0, valor)
#             print(f'O valor {valor} foi adicionado na posicao 0')
#
#     if cont == 3:
#         if valor > valores[2]:
#             valores.insert(3, valor)
#             print(f'O valor {valor} foi adcionado ao final da lista')
#
#         if valor >= valores[1] and valor < valores[2]:
#             valores.insert(2, valor)
#             print(f'O valor {valor} foi adicionado na posicao 2')
#
#         if valor >= valores[0] and valor <= valores[1]:
#             valores.insert(1, valor)
#             print(f'O valor {valor} foi adicionado na posicao 1')
#
#         if valor < valores[0]:
#             valores.insert(0, valor)
#             print(f'O valor {valor} foi adicionado na posicao 0')
#
#     if cont == 4:
#         if valor > valores[3]:
#             valores.insert(4, valor)
#             print(f'O valor {valor} foi adcionado ao final da lista')
#
#         if valor >= valores[2] and valor < valores[3]:
#             valores.insert(3, valor)
#             print(f'O valor {valor} foi adicionado na posicao 3')
#
#         if valor >= valores[1] and valor <= valores[2]:
#             valores.insert(2, valor)
#             print(f'O valor {valor} foi adicionado na posicao 2')
#
#         if (valor > valores[0] and valor <= valores[1]):
#             valores.insert(1, valor)
#             print(f'O valor {valor} foi adicionado na posicao 1')
#
#         if valor < valores[0]:
#             valores.insert(0, valor)
#             print(f'O valor {valor} foi adicionado na posicao 0')
#
# print('=-' * 30)
# print(f'Os valores digitados em ordem foram: {valores}')

########## PROFESSOR ############
lista = list()

for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores em ordem digitados foram {lista}')
