# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


# def contador(inicio, fim, passo):
#
#     if passo == 0:
#         passo = 1
#     if fim > inicio:
#         if passo < 0:
#             passo = +passo
#     if inicio > fim:
#         if passo > 0:
#             passo = -passo
#     print(f'Contagem de {inicio} até {fim} de {str(passo).replace("-", "")} em '
#           f'{str(passo).replace("-", "")}')
#     if passo > 0:
#         for contador2 in range(inicio, fim + 1, passo):
#             sleep(0.3)
#             print(contador2, end=' ')
#         print('FIM!')
#     if passo <= 0:
#         for contador2 in range(inicio, fim - 1, passo):
#             sleep(0.3)
#             print(contador2, end=' ')
#         print('FIM!')
#
#
# contador(1, 10, 1)
# contador(10, 0, -2)
# print('Agora é sua vez de personalizar a contagem')
# comeco = int(input('Inicio:'))
# final = int(input('Fim:'))
# contagem = int(input('Passo:'))
# contador(comeco, final, contagem)


#### PROFESSOR

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print("FIM!")


contador(1, 10, 1)
contador(10, 0, -2)
print('=-' * 20)
print('Agora é sua vez de personalizar a contagem')
comeco = int(input('Inicio:'))
final = int(input('Fim:'))
contagem = int(input('Passo:'))
contador(comeco, final, contagem)
