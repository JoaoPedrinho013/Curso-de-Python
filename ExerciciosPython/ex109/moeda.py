# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.


def aumentar(preco=0, taxa=0, conversor=False):
    num = preco + (preco * taxa / 100)
    return num if conversor is False else moeda(num)

def diminuir(preco=0, taxa=0, conversor=False):
    num = preco - (preco * taxa / 100)
    return num if not conversor else moeda(num)


def dobro(preco=0, conversor=False):
    num = preco * 2
    if conversor == False:
        return num
    else:
        return moeda(num)


def metade(preco=0, conversor=False):
    num = preco / 2
    if conversor:
        return moeda(num)
    else:
        return num


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
