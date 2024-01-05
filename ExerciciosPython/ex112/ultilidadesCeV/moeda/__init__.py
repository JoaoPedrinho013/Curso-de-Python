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


def resumo(preco=0, aumento=0, reducao=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço:  \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento:  \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução:  \t{diminuir(preco, reducao, True)}')
    print('-' * 30)
