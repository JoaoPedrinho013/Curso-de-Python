# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.


def aumentar(preco=0, taxa=0):
    num = preco + (preco * taxa / 100)
    return num


def diminuir(preco=0, taxa=0):
    num = preco - (preco * taxa / 100)
    return num


def dobro(preco=0):
    num = preco * 2
    return num


def metade(preco=0):
    num = preco / 2
    return num

def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

