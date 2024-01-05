def linha(tamanho=50):
    return '\033[97m-\033[m' * tamanho


def cabecalho(texto=''):
    print(linha())
    print('\033[92m' + texto.center(50).upper())
    print(linha())


def leiaInt(pergunta=''):
    while True:
        try:
            inteiro = int(input(pergunta))
        except:
            print(f'\033[91mErro. Por favor digite um número inteiro válido\033[m')
        else:
            return inteiro


def menu(lista):
    cabecalho('Menu principal')
    contador = 1
    for item in lista:
        print(f'\033[93m{contador} -  \033[94m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[93mSua opção: \033[m')
    return opcao
