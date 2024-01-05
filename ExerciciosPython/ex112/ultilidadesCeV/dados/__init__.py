def leiaDinheiro(texto=''):
    while True:
        pergunta = str(input(texto)).replace(',', '.').strip()
        if pergunta.isalpha() or pergunta == '':
            print(f'\033[1;91mERRO: "{pergunta}" é um preço invalido\033[m')
        else:
            pergunta = float(pergunta)
            break
    return pergunta

def leiaInt(pergunta=''):
    while True:
        try:
            inteiro = int(input(pergunta))
        except (ValueError, TypeError):
            print(f'\033[91mErro. Por favor digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[91mUsuario preferiu nao digitar o numero\033[m')
            return 0
        else:
            return inteiro


def leiaFloat(pergunta=''):
    while True:
        try:
            real = float(input(pergunta))
        except (ValueError, TypeError):
            print(f'\033[91mErro. Por favor digite um número real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[91mUsuario preferiu nao digitar o numero\033[m')
            return 0
        else:
            return real
