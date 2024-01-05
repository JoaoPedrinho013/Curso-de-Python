# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.


# inicio = '\033[1:92:47m'
# informacao = '\033[1:92:40m'
# fim = '\033[1:91:47m'
# limpar = '\033[0:0:0m'
#
#
# def verificacao():
#     while True:
#         pergunta = input('Função ou biblioteca:')
#         if pergunta.strip().lower() == 'fim':
#             print(fim, '-=' * 20, )
#             print('            FIM DO PROGRAMA             ')
#             print('-=' * 20)
#             print(limpar)
#             break
#         print(informacao)
#         help(pergunta)
#         print(limpar)
#
#
#
# print(inicio, '-=' * 20)
# print('        SISTEMA DE AJUDA PYTHON         ')
# print('-=' * 20)
# print(limpar)
# verificacao()


from time import sleep

c = ['\033[m',         # 0 SEM COR
     '\033[0;30;41m',  # 1 VERMELHO
     '\033[0;30;42m',  # 2 VERDE
     '\033[0;30;43m',  # 3 AMARELO
     '\033[0;30;44m',  # 4 AZUL
     '\033[0;30;45m',  # 5 ROXO
     '\033[7m']  # 6 BRANCO


def ajuda(com):
    titulo(f'Acessando o manual do comando\'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# PROGRAMA PRINCIPAL

comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
