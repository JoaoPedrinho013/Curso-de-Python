# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

numeros = []


def sorteia():
    """

    :return:
    """
    print(f'Sorteando os 6 valores da lista: ', end='')
    for contador in range(5):
        numeros.append(randint(1, 10))
    for valor in numeros:
        print(valor, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar():
    """

    :return:
    """
    soma = 0
    for indice, valor in enumerate(numeros):
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()

somaPar()
