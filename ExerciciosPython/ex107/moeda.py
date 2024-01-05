# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
# e use algumas dessas funções.

def aumentar(preco, taxa):
    num = preco + (preco * taxa / 100)
    return num


def diminuir(preco, taxa):
    num = preco - (preco * taxa / 100)
    return num


def dobro(preco):
    num = preco * 2
    return num


def metade(preco):
    num = preco / 2
    return num
