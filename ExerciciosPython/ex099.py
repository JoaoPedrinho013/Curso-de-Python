# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*valores):
    """

    :param valores:
    :return:
    """
    cont = maior_valor = 0
    print('=-' * 30)
    print('Analisando os valores passados...')
    for valor in valores:
        cont += 1
        if cont == 1:
            maior_valor = valor
        if valor > maior_valor:
            maior_valor = valor
        print(valor, end=' ')
        sleep(0.5)

    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi o {maior_valor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
