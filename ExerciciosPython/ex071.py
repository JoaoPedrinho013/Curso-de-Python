# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
                #### PRIMEIRO TESTE ######
# print('=' * 35)
# print('SEJA BEM VINDO AO BANCO DA MACONHA!')
# print('=' * 35)
# grana = int(input('Qual valor você quer sacar? R$'))
# while True:
#     if grana >= 50:
#         nota50 = grana // 50
#         sub = nota50 * 50
#         grana -= sub
#         print(f'Total de {nota50} notas de R$50')
#     if grana >= 20:
#         nota20 = grana // 20
#         sub2 = nota20 * 20
#         grana -= sub2
#         print(f'Total de {nota20} notas de R$20')
#     if grana >= 10:
#         nota10 = grana // 10
#         sub3 = nota10 * 10
#         grana -= sub3
#         print(f'Total de {nota10} notas de R$10')
#     if grana >= 1:
#         nota1 = grana // 1
#         sub4 = nota1 * 1
#         grana -= sub4
#         print(f'Total de {nota1} notas de R$1')
#     if grana == 0:
#         break
# print('=' * 35)
# print('Volte sempre ao Banco da Maconha!!! Bom dia!')

              ##### SEGUNDO TESTE #####
# aqui so comeca a partir do 50 mas se eu inverter a logica da pra comecar a partir do 1 #

# print('='30)
# print('         BANCO LIGHT')
# print('='30)
# valor = int(input('Qual valor vc quer sacar? R$'))
# numero = 50
# while True:
#     if valor >= numero:
#         cedula = valor // numero
#         sub = cedula * numero
#         valor -= sub
#         print(f'total de {cedula} cédulas de {numero}')
#     numero = 20
#     if valor >= numero:
#         cedula = valor // numero
#         sub = cedula * numero
#         valor -= sub
#         print(f'total de {cedula} cédulas de {numero}')
#     numero = 10
#     if valor >= numero:
#         cedula = valor // numero
#         sub = cedula * numero
#         valor -= sub
#         print(f'total de {cedula} cédulas de {numero}')
#     numero = 1
#     if valor == 0:
#         break
# print('='*30)
# print('Volte sempre ao BANCO LIGHT')

                ##### CHAT GPT #####
# print('=' * 35)
# print('SEJA BEM VINDO AO BANCO DA MACONHA!')
# print('=' * 35)
#
# grana = int(input('Qual valor você quer sacar? R$'))
# notas = [50, 20, 10, 1]
# contador = 0
#
# while True:
#     nota = notas[contador]
#     if grana >= nota:
#         quantidade = grana // nota
#         grana %= nota
#         print(f'Total de {quantidade} notas de R${nota}')
#     contador += 1
#     if grana == 0:
#         break
#
# print('=' * 35)
# print('Volte sempre ao Banco da Maconha!!! Bom dia!')

                 #### JEITO PROFESSOR ####

print('=' * 35)
print('{:^30}'.format('BANCO CEV'))
print('=' * 35)

valor = int(input('Que valor voce quer sacar?'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas  de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 35)
print('Volte sempre ao Banco da Maconha!!! Bom dia!')